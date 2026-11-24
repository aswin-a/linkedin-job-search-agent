#!/usr/bin/env python3
"""Deterministic checks for a FINAL resume exported as HTML.

Implements the machine-checkable parts of
skills/tailored-resume/references/skim-formatting.md and the ATS-safe rules.
It cannot judge truthfulness or relevance; those need the mapping doc and a human.

Usage:
    python3 evals/check_resume_format.py RESUME.html [--pages N]

Exit code 0 if no check FAILs (WARNs are allowed), 1 otherwise.
Standard library only.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser

SOFT_WORDS = {"strong", "cross-functional", "stakeholders", "stakeholder", "team", "successfully"}
NO_BOLD_SECTIONS = ("core skills", "skills", "education", "certifications")
SUMMARY_SECTIONS = ("summary", "professional summary")
FORBIDDEN_TAGS = {"table", "img", "i", "em", "u", "font", "svg", "style", "script"}
REQ_ID = re.compile(r"\(\s*[MN]\d+(?:\s*,\s*[MN]\d+)*\s*\)")
DATE_LIKE = re.compile(r"^(?:[A-Z][a-z]{2}\s+\d{4}|\d{4})(?:\s*[–-]\s*(?:[A-Z][a-z]{2}\s+\d{4}|\d{4}|Present))?$")


@dataclass
class Bullet:
    section: str
    role: int
    text: str = ""
    bolds: list[str] = field(default_factory=list)


@dataclass
class Doc:
    bullets: list[Bullet] = field(default_factory=list)
    summary_bolds: list[str] = field(default_factory=list)
    other_bolds: list[tuple[str, str]] = field(default_factory=list)  # (section, text) in <p> outside summary
    forbidden: set[str] = field(default_factory=set)
    styled: int = 0
    text: list[str] = field(default_factory=list)
    roles_per_section: dict[str, int] = field(default_factory=dict)


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.doc = Doc()
        self.section = ""
        self.role = 0
        self.stack: list[str] = []
        self.bullet: Bullet | None = None
        self.bold_buf: list[str] | None = None
        self.h2_buf: list[str] | None = None
        self.in_p = False
        self.p_has_bold = False

    def handle_starttag(self, tag, attrs):
        if tag in FORBIDDEN_TAGS:
            self.doc.forbidden.add(tag)
        if any(k == "style" for k, _ in attrs):
            self.doc.styled += 1
        self.stack.append(tag)
        if tag == "h2":
            self.h2_buf = []
        elif tag == "li":
            self.bullet = Bullet(self.section, self.role)
        elif tag in ("b", "strong"):
            self.bold_buf = []
        elif tag == "p":
            self.in_p = True
            self.p_has_bold = False

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        if tag == "h2" and self.h2_buf is not None:
            self.section = " ".join("".join(self.h2_buf).split()).lower()
            self.role = 0
            self.h2_buf = None
        elif tag in ("b", "strong") and self.bold_buf is not None:
            text = " ".join("".join(self.bold_buf).split())
            self.bold_buf = None
            if "h1" in self.stack or "h2" in self.stack or self.h2_buf is not None:
                return  # name / section headings are allowed bold
            if self.bullet is not None:
                self.bullet.bolds.append(text)
            elif self.in_p:
                self.p_has_bold = True
                if self.section in SUMMARY_SECTIONS:
                    self.doc.summary_bolds.append(text)
                else:
                    self.doc.other_bolds.append((self.section, text))
        elif tag == "li" and self.bullet is not None:
            self.bullet.text = " ".join(self.bullet.text.split())
            self.doc.bullets.append(self.bullet)
            self.bullet = None
        elif tag == "p":
            # A <p> with a bold title outside summary/skills sections starts a new role.
            if self.p_has_bold and self.section not in SUMMARY_SECTIONS:
                self.role += 1
                self.doc.roles_per_section[self.section] = self.role
            self.in_p = False

    def handle_data(self, data):
        self.doc.text.append(data)
        if self.h2_buf is not None:
            self.h2_buf.append(data)
        if self.bold_buf is not None:
            self.bold_buf.append(data)
        if self.bullet is not None:
            self.bullet.text += data


@dataclass
class Result:
    level: str  # PASS / WARN / FAIL
    name: str
    detail: str = ""


def check(html: str, pages: int) -> list[Result]:
    p = Parser()
    p.feed(html)
    d = p.doc
    out: list[Result] = []

    def add(ok: bool, name: str, detail: str = "", warn_only: bool = False):
        out.append(Result("PASS" if ok else ("WARN" if warn_only else "FAIL"), name, "" if ok else detail))

    add(not d.forbidden, "ATS-safe tags (no tables, images, italics, underline)", f"found: {sorted(d.forbidden)}")
    add(d.styled == 0, "No inline styles", f"{d.styled} element(s) with style=")

    full = " ".join(" ".join(d.text).split())
    ids = REQ_ID.findall(full)
    add(not ids, "No requirement-ID tags left in the resume", f"found: {ids[:5]}")

    multi = [b for b in d.bullets if len(b.bolds) > 1]
    add(not multi, "At most one bold phrase per bullet", "; ".join(b.text[:50] for b in multi[:3]))

    whole = [b for b in d.bullets if b.bolds and b.bolds[0].strip(" .") == b.text.strip(" .")]
    add(not whole, "No whole-bullet bold", "; ".join(b.text[:50] for b in whole[:3]))

    skim = [t for b in d.bullets for t in b.bolds] + d.summary_bolds
    bad_len = [t for t in skim if not 2 <= len(t.split()) <= 6]
    add(not bad_len, "Bold phrases are 2-6 words", f"{bad_len[:5]}")

    soft = [t for t in skim if SOFT_WORDS & {w.strip(",.;:").lower() for w in t.split()}]
    add(not soft, "No soft words in bold", f"{soft[:5]}")

    dates = [t for t in skim + [t for _, t in d.other_bolds] if DATE_LIKE.match(t)]
    add(not dates, "No bold dates", f"{dates[:5]}")

    in_banned = [b.text[:40] for b in d.bullets if b.bolds and b.section.startswith(NO_BOLD_SECTIONS)]
    in_banned += [t for s, t in d.other_bolds if s.startswith(NO_BOLD_SECTIONS)]
    add(not in_banned, "No bold in Core Skills / Education / Certifications", f"{in_banned[:5]}")

    add(len(d.summary_bolds) <= 2, "Summary has at most 2 bold phrases", f"{len(d.summary_bolds)} found")

    n = len(skim)
    add(8 <= n <= 14, "8-14 skim bold phrases in total", f"{n} found", warn_only=True)

    roles: dict[tuple[str, int], list[Bullet]] = {}
    for b in d.bullets:
        if b.role:
            roles.setdefault((b.section, b.role), []).append(b)
    all_bold = [k for k, bs in roles.items() if len(bs) >= 3 and all(b.bolds for b in bs)]
    add(not all_bold, "Not every bullet in a role is bold", f"{len(all_bold)} role(s) fully bolded", warn_only=True)

    words = len(full.split())
    lo, hi = 450 * pages, 550 * pages
    add(lo <= words <= hi, f"Word count {lo}-{hi} for {pages} page(s)", f"{words} words", warn_only=True)

    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("resume", help="FINAL resume exported as HTML")
    ap.add_argument("--pages", type=int, default=1, help="target page count (default 1)")
    args = ap.parse_args(argv)
    with open(args.resume, encoding="utf-8") as fh:
        results = check(fh.read(), args.pages)
    for r in results:
        print(f"{r.level:4}  {r.name}" + (f"  ->  {r.detail}" if r.detail else ""))
    fails = sum(r.level == "FAIL" for r in results)
    warns = sum(r.level == "WARN" for r in results)
    print(f"\n{args.resume}: {fails} fail, {warns} warn, {len(results) - fails - warns} pass")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
