# Public-source preflight checks

The repository includes a small **offline, read-only** guard for accidental release of raw Oracle APEX exports and a few common API secret patterns. It requires Python 3.10+ and **does not execute SQL, upload data, use network services, or require GitHub Actions**.

Run from the repository root:

```sh
python -m unittest discover -s tests -v
python scripts/check_public_release.py .
```

To check a proposed source file before publication:

```sh
python scripts/check_public_release.py /path/to/candidate.sql
```

Nonzero status means review or block. The script prints file paths and finding categories, **not secret contents**. It intentionally blocks raw `f123.sql` APEX export names, ZIP/backup archives and common token-shaped patterns even when their contents might be harmless. Renaming a file to avoid a check is not security review.

**Limitations:** This is not comprehensive secret detection, a Git history scanner, binary embedded-asset analysis, SQL parser, code safety proof, or redistribution/license authorization. Scanning the current checkout cannot detect secrets retained in prior Git commits, cached objects, downloads or forks.

## Confirmed source-specific review findings

- Two configured authentication schemes, one selected for public access; a second Oracle APEX Accounts scheme is defined but not shown as active.
- Administration Rights scheme evaluates `return true;`, which does not implement an administrative privilege check.
- Two external web sources and literal API key values are present in the supplied export, independent of whether features are currently used on the public demo.

Read [APEX export findings](APEX_EXPORT_FINDINGS.md). Do not change the deployed Oracle APEX application based on static findings alone.

## Required manual release review

1. Rotate/revoke any historically exposed OpenAI/RapidAPI credentials in the provider consoles and replace usages in live APEX with protected server-side credentials. Review billing/usage logs.
2. Assess the removed historical ZIP and all other Git history. Follow GitHub sensitive-data-removal guidance when appropriate; coordinate any invasive history rewrite.
3. Review export metadata, personal information, embedded binary/static assets and third-party redistribution rights.
4. Provision and test required Oracle schema and importable APEX application in an authorized isolated environment. The public README is **not** proof of a working install.
5. Publish a sanitized export only after those gates pass, with an explicit license and tested installation instructions.

Local QA on the initial guard implementation (Python 3 runtime in tool environment): **8 unit tests passed**, plus a clean-sample scan passed; the original owner-uploaded `f238769.sql` was blocked because it is an unreviewed raw export. The guard also blocks the known unsafe `Administration Rights` function body `return true;` in raw APEX export SQL. A targeted real-export assertion and two synthetic examples verified this rule's intended behavior; the whole revised Git checkout test suite is not yet independently executed. The script does not establish that the public ZIP (since deleted from current main) had identical bytes.
