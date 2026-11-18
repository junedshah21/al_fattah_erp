# Security incident response — historical APEX export

**Status: ACTION REQUIRED by the credential owner.** This document contains no secret values and does not mean any key has been revoked. Based on the owner's supplied `f238769.sql` from 2026-11-18.

## Verified facts

- The reviewed Oracle APEX export contains **two OpenAI secret-key-shaped literals**, an inline `x-rapidapi-key` configuration value, and remote API references.
- The export also includes creator metadata, email addresses and embedded static files.
- The previously uploaded public `al-fattah-erp.zip` has been deleted from current `main`; exact ZIP contents were **not independently verified**. Old commits can retain the archive.
- The APEX app is described by its owner as a public demo. Public access does **not** prove API keys are absent or inaccessible in SQL exports.
- The `Administration Rights` authorization scheme in the export unconditionally returns `true`; current runtime exposure has not been verified.

## Immediate provider actions (owner only)

1. Sign in to the **OpenAI Platform** project(s) that issued the historical keys. Identify each exposed key by comparing privately with the original export; **delete/revoke both old keys**, then create replacement keys only for services still actually needed. Do not paste key values into GitHub, ChatGPT, screenshots or tickets.
2. Sign in to **RapidAPI**. Revoke/regenerate the exposed credential following the provider's supported controls and update any surviving integrations.
3. Review OpenAI and RapidAPI usage/billing for suspicious requests after publication. Escalate to provider support if necessary.
4. Confirm revoked credentials can no longer authenticate. Record only nonsecret confirmation and dates.
5. In **the deployed APEX workspace**, remove literals from source; prefer properly scoped server-side **APEX Web Credentials** for integrations that remain in use. Disable unused integrations and test all affected APEX pages. Do not deploy this project's review-only export in place of the running application.

## GitHub historical exposure

1. Verify which historical commit held `al-fattah-erp.zip` and assess the file securely. Do not repost the bytes or secrets to public issues.
2. Revoke credentials **before** history cleanup: deleting Git objects does not invalidate credentials already copied.
3. Follow GitHub's [official sensitive-data-removal procedure](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). It describes `git-filter-repo --sensitive-data-removal`, reviewing affected pull requests, force-pushing rewritten refs, and coordinating collaborators/forks.
4. **Do not force-push blindly.** Rewriting Git history changes commit IDs, may invalidate signatures, disrupt forks/clones, and may not erase caches or other copies. Ensure all collaborators have been informed and verify sensitive references after remediation.
5. If GitHub support assistance is needed, follow the official process. Do not provide public credentials in an issue. GitHub may not purge data if risk is already mitigated by revoking affected credentials.

## Source release gates

- The public source **must not include** production credentials, unreviewed embedded assets, personal data or confidential records.
- Choose and verify an OSS license only for material the maintainer has rights to redistribute.
- Supply schema DDL and dependencies if claiming that the ERP is installable. Existing `f238769.sql` lacks standalone `CREATE TABLE` statements in a basic scan.
- Run `python -m unittest discover -s tests -v` and `python scripts/check_public_release.py .` against an authorized checkout. The latter detects only a small set of patterns and **does not scan Git history**.
- Independently test application import and public page/process authorization before claiming production-grade security.

**What this repository has already done:** deleted unsafe ZIP from current `main`, added local guard and unit tests, and documented source-level findings. **What it has not done:** rotate external service credentials, change the running APEX application, purge old Git objects, or validate a full ERP installation.
