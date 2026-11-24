#!/usr/bin/env python3
"""Repo lint: SKILL.md frontmatter + relative Markdown links.

Skills (skills/*/SKILL.md):
  - frontmatter block parses (--- ... ---, `key: value` lines)
  - `name` is kebab-case, <= 64 chars, and matches the folder name
  - `description` is present, <= 1024 chars, and says when to trigger ("Use when")
  - body has the Inputs / Outputs / Stop conditions block

Links (every tracked *.md):
  - every relative link target exists
  - every #anchor into a Markdown file matches a heading (GitHub slug rules)

Usage: python3 scripts/lint_repo.py      Standard library only. Exit 1 on any error.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"^(```|~~~)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("no opening '---'")
    try:
        end = next(i for i, l in enumerate(lines[1:], 1) if l.strip() == "---")
    except StopIteration:
        raise ValueError("no closing '---'") from None
    meta: dict[str, str] = {}
    for n, line in enumerate(lines[1:end], 2):
        if not line.strip():
            continue
        if ":" not in line or line.startswith((" ", "\t")):
            raise ValueError(f"line {n}: expected 'key: value', got {line!r}")
        key, val = line.split(":", 1)
        meta[key.strip()] = val.strip().strip('"').strip("'")
    return meta, "\n".join(lines[end + 1 :])


def lint_skills() -> list[str]:
    errors: list[str] = []
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("no skills/*/SKILL.md found")
    for path in skills:
        rel = path.relative_to(ROOT)
        try:
            meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        except ValueError as e:
            errors.append(f"{rel}: frontmatter: {e}")
            continue
        name, desc = meta.get("name", ""), meta.get("description", "")
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{rel}: name {name!r} is not kebab-case <= 64 chars")
        if name != path.parent.name:
            errors.append(f"{rel}: name {name!r} != folder {path.parent.name!r}")
        if not desc:
            errors.append(f"{rel}: missing description")
        elif len(desc) > 1024:
            errors.append(f"{rel}: description is {len(desc)} chars (> 1024)")
        elif "use when" not in desc.lower():
            errors.append(f"{rel}: description doesn't say when to trigger ('Use when ...')")
        for label in ("**Inputs**", "**Outputs**", "**Stop conditions**"):
            if label not in body:
                errors.append(f"{rel}: missing {label} in the I/O block")
        print(f"ok    {rel}  (name={name}, description={len(desc)} chars)")
    return errors


def slug(heading: str) -> str:
    s = re.sub(r"[`*_~]|<[^>]+>", "", heading.strip().lower())
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def anchors(md: Path) -> set[str]:
    out: set[str] = set()
    seen: dict[str, int] = {}
    in_fence = False
    for line in md.read_text(encoding="utf-8").splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
        if in_fence:
            continue
        m = re.match(r"^#{1,6}\s+(.*?)\s*#*$", line)
        if m:
            base = slug(m.group(1))
            n = seen.get(base, 0)
            out.add(base if n == 0 else f"{base}-{n}")
            seen[base] = n + 1
    return out


def lint_links() -> list[str]:
    errors: list[str] = []
    tracked = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "*.md"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout.split()
    count = 0
    for relpath in tracked:
        md = ROOT / relpath
        in_fence = False
        for n, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if FENCE_RE.match(line.strip()):
                in_fence = not in_fence
            if in_fence:
                continue
            for target in LINK_RE.findall(line):
                if re.match(r"^[a-z]+:", target):  # http:, https:, mailto:
                    continue
                count += 1
                file_part, _, frag = target.partition("#")
                dest = (md.parent / file_part).resolve() if file_part else md
                if not dest.exists():
                    errors.append(f"{relpath}:{n}: broken link -> {target}")
                elif frag and dest.suffix == ".md" and frag not in anchors(dest):
                    errors.append(f"{relpath}:{n}: missing anchor -> {target}")
    print(f"ok    checked {count} relative links in {len(tracked)} Markdown files")
    return errors


def main() -> int:
    errors = lint_skills() + lint_links()
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
