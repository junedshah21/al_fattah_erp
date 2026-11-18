# APEX export: verified configuration findings

Source: the project owner's locally supplied `f238769.sql` application export (18 November 2026). This is a **read-only static analysis**, not evidence that the corresponding feature is currently used by the running website. No credential values are included here.

## Authentication and authorization

- Application's selected authentication scheme is named **Create for public**, with APEX scheme type `NATIVE_DAD` and username setting `testing`. It does not establish that login is required for visitors.
- A second scheme named **Oracle APEX Accounts** (`NATIVE_APEX_ACCOUNTS`) also exists in the export. Its existence does **not** prove that it is the active scheme.
- The **Administration Rights** authorization scheme is a `NATIVE_FUNCTION_BODY` whose PL/SQL expression is `return true;`. This means the scheme itself does not restrict administration privileges. Whether components depend on the scheme or whether they are publicly reachable was **not** verified. Do not treat this scheme as production-grade protection.

## External integrations present in export

- Two APEX web-source modules: **GeoDB Cities** and **Quran Sharif**.
- Remote-server definitions reference a GeoDB RapidAPI endpoint and an AlQuran Cloud endpoint.
- Web-source settings include an **inline RapidAPI credential value**. The value is deliberately omitted.
- Two **OpenAI API-key-shaped literal occurrences** were found in PL/SQL associated with outbound requests; the source also mentions OpenAI's chat-completions endpoint.
- Whether any of these services is currently called by live users **has not been established**. The user's description of a public/no-login demo does not imply the export has no API references.

## Public source and live demo are different

Publishing a website makes its rendered functionality accessible. Publishing an APEX export also reveals embedded code, workspace metadata, external service settings and static assets. The current GitHub repository deliberately contains **no raw or redacted application export** until secrets, rights and install dependencies receive a complete review. A previous public ZIP was removed from current main but may remain in Git history.

## Required actions outside this repository

1. Revoke or rotate affected OpenAI and RapidAPI credentials using the corresponding providers, even if the API-backed features are no longer used. Review unexpected usage/billing.
2. In the owner's live APEX environment, eliminate hard-coded keys and use protected server-side credentials, or safely remove the integrations if confirmed unused.
3. Assess the `return true;` authorization scheme against every component it guards. Restrict or remove administrative functions as appropriate.
4. Check historic Git exposure and third-party rights before distributing a sanitized export.
5. Verify publicly accessible pages and processes in a controlled browser/Oracle environment.

**Status:** The repository documents these findings; it has not changed the live Oracle APEX application, revoked provider credentials, or proven installability.
