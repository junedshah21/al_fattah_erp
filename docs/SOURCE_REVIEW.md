# Source review summary (2026-11-18)

Source inspected locally: `f238769.sql`; approximately 9.15 MB. APEX Application ID 238769, name AL-FATTAH ERP.

| Inventory from export header | Count |
|---|---:|
| Pages | 13 |
| Regions | 76 |
| Items | 44 |
| Processes | 14 |
| Buttons | 12 |
| Dynamic actions | 9 |
| Authentication schemes | 2 |
| Authorization schemes | 1 |
| Web source modules | 2 |

**Security findings:** two OpenAI API-key occurrences, one RapidAPI key; exporter identity and external service metadata; embedded static files. This summary intentionally contains no secret values. The previously public ZIP was removed from current main in commit `668b8df97f778ef1ddf357dace79051ce4d7003d`, but it has not been independently downloaded/decompressed to confirm its precise bytes, and old Git history may still expose it.

**Limitations:** no Oracle runtime execution; no standalone database schema DDL detected in a simple textual scan; no full-license/third-party assets audit; no comprehensive encoded-secret scan; no external adoption verified. The original export and previously public ZIP must not be treated as a reviewed or safe open-source release.
