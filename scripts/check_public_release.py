#!/usr/bin/env python3
"""Conservative pre-publication guard for AL-FATTAH ERP.

Scans selected files or recursively scans a folder; never executes input.
This is not a substitute for full secret scanning or a license/privacy audit.
"""
import argparse
from pathlib import Path
import re
import sys

BAD_EXTENSIONS = {".zip", ".7z", ".rar", ".dmp", ".bak", ".p12", ".pfx", ".pem", ".key"}
BAD_NAME = re.compile(r"^f\d+\.sql$", re.I)
RULES = {
    "openai_key": re.compile(rb"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    "github_token": re.compile(rb"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "aws_access_key": re.compile(rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "private_key_header": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----"),
    "rapidapi_inline_header": re.compile(rb"(?i)(?:x-rapidapi-key)[^\r\n]{0,220}?(?:p_value\s*=>\s*'[^']{12,}'|[:=]\s*['\"]?[a-z0-9_-]{25,})"),
}
IGNORE_PARTS = {".git", ".venv", "__pycache__", "node_modules", ".pytest_cache"}
MAX_BYTES = 25 * 1024 * 1024


def scan(path: Path):
    """Return (display_path, problem_code) entries, never secret values."""
    problems = []
    paths = (p for p in path.rglob("*") if p.is_file() and not (set(p.parts) & IGNORE_PARTS)) if path.is_dir() else (path,)
    for p in paths:
        label = str(p)
        if p.suffix.lower() in BAD_EXTENSIONS or BAD_NAME.fullmatch(p.name):
            problems.append((label, "unreviewed_export_or_archive"))
            continue
        try:
            if p.stat().st_size > MAX_BYTES:
                problems.append((label, "file_too_large_to_scan"))
                continue
            b = p.read_bytes()
        except OSError:
            problems.append((label, "unreadable_file"))
            continue
        for name, rx in RULES.items():
            if rx.search(b):
                problems.append((label, name))
    return problems


def main(argv=None):
    parser = argparse.ArgumentParser(description="Fail a public release on obvious unreviewed archives or suspected keys.")
    parser.add_argument("path", nargs="?", default=".", type=Path)
    args = parser.parse_args(argv)
    if not args.path.exists():
        print("ERROR: requested path does not exist", file=sys.stderr)
        return 2
    issues = scan(args.path)
    if issues:
        for path, code in issues:
            print(f"BLOCK: {path}: {code}")
        print(f"FAIL: {len(issues)} potential release issue(s); review privately. No secret values printed.")
        return 1
    print("PASS: no matches to this limited local rule set. Manual review still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
