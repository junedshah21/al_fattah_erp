# AL-FATTAH ERP — Oracle APEX demo

AL-FATTAH ERP is an independently developed Oracle APEX demonstration application (Application ID **238769**). This repository currently documents the project and a public demo. **The reviewed export is not a complete, security-cleared, turnkey ERP release.**

**Live demo:** https://oracleapex.com/ords/f?p=238769:1:

## Verified from Oracle APEX export (2026-11-18)

| Component | Count |
| --- | ---: |
| Pages | 13 |
| Regions | 76 |
| Page items | 44 |
| Page processes | 14 |
| Buttons | 12 |
| Dynamic actions | 9 |
| Authentication schemes | 2 |
| Authorization schemes | 1 |
| Web source modules | 2 |

Named areas include Home, ERP Details, ERP Modules, Create Terms Request, View Attachment, About Us, an Oracle APEX interview page and standard application utility screens. These are **static export findings**, not independent runtime or full ERP-module validation.

## Technology

Oracle APEX, Oracle Database, SQL and PL/SQL. The export uses native APEX pages, shared components, static assets and external web-source definitions.

## Current repository scope

This is a **public project overview**, not a verified installable release. The source export may reference external services, workspace credentials, static assets and database objects unavailable in the export. The exported SQL has **no standalone CREATE TABLE DDL** according to a simple text scan, so it is not sufficient evidence of a full installable ERP database.

**Security:** The potentially unsafe `al-fattah-erp.zip` was removed from the current main branch in security commit `668b8df97f778ef1ddf357dace79051ce4d7003d`. Earlier Git history may still retain the archive, and its exact contents were not independently inspected. Do not download/reuse any credentials. Owner action to revoke/rotate keys and assess historical exposure remains required; see [SECURITY.md](SECURITY.md). A sanitized source release will only be included after comprehensive review.

## Public-release safety checks

Before adding application exports or releases, run the offline check: `python scripts/check_public_release.py .` and tests: `python -m unittest discover -s tests -v`. This only detects a limited set of risks; see [release checklist](docs/RELEASE_CHECKLIST.md). Historical Git objects and revoked/rotated credentials need independent review.

## Project status

- Application authored and hosted by project maintainer (owner statement).
- Static APEX export reviewed on 2026-11-18.
- No live import, end-to-end tests, full database installation or independent security certification claimed.
- Community contributions welcome after release scope and licensing are confirmed; see [CONTRIBUTING.md](CONTRIBUTING.md).

This independent project is not affiliated with Oracle or OpenAI. Oracle and APEX are trademarks of Oracle and its affiliates.
