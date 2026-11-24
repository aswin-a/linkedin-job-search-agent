#!/usr/bin/env bash
# Privacy check: fail if repo files contain anything that looks like personal data:
# Google Drive/Docs/Sheets IDs, salary figures (LPA / CTC amounts), email
# addresses or phone numbers. Run before every commit.
#
# Usage: scripts/check_privacy.sh   (scans tracked + untracked, non-ignored files)
set -uo pipefail
cd "$(git rev-parse --show-toplevel)"

mapfile -t files < <(git ls-files --cached --others --exclude-standard | grep -v '^scripts/check_privacy.sh$')
fail=0

report() { # label, hits
  if [[ -n "$2" ]]; then
    echo "FAIL  $1"; echo "$2" | sed 's/^/      /'; fail=1
  else
    echo "PASS  $1"
  fi
}

scan() { # pattern [allow-pattern]
  grep -nIE "$1" "${files[@]}" 2>/dev/null | { if [[ -n "${2:-}" ]]; then grep -vE "$2"; else cat; fi; } || true
}

# Google IDs: tokens of 25+ chars from [A-Za-z0-9_-] mixing upper case, lower case and digits
# (real Drive/Docs/Sheets IDs do; lowercase hyphenated slugs and long words don't).
ids=$(grep -noIE '[A-Za-z0-9_-]{25,}' "${files[@]}" 2>/dev/null \
      | awk -F: '{t=$NF} t ~ /[0-9]/ && t ~ /[A-Z]/ && t ~ /[a-z]/' || true)
report "Google-ID-like tokens (25+ chars, mixed case + digits)" "$ids"

report "Salary figures (LPA / lakh / CTC / INR amounts)" "$(scan \
  '[0-9]+(\.[0-9]+)?[[:space:]]*(LPA|lpa|[Ll]akhs?)|(CTC|ctc)[^|]{0,20}[0-9]{2,}|₹[[:space:]]*[0-9]|INR[[:space:]]*[0-9]')"

report "Email addresses (except example / noreply domains)" "$(scan \
  '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' \
  '@(([A-Za-z0-9-]+\.)*example(\.[a-z]+)?|users\.noreply\.github\.com|anthropic\.com)([^A-Za-z]|$)')"

report "Phone numbers" "$(scan \
  '(\+91[[:space:]-]?)?[6-9][0-9]{4}[[:space:]-]?[0-9]{5}([^0-9]|$)|\+[0-9]{1,3}[[:space:]-][0-9]{3,5}[[:space:]-]?[0-9]{3,5}')"

echo
if [[ $fail -ne 0 ]]; then echo "Privacy check FAILED"; exit 1; fi
echo "Privacy check passed (${#files[@]} files)"
