# Installation and deployment status

The application export was generated with Oracle APEX **26.2.1** release metadata, and the application reports compatibility mode **24.2**. This is static export metadata, not a tested installation matrix.

**Do not run the original export from the public ZIP until secrets, dependencies, and ownership of embedded assets have been reviewed.**

The supplied export contains the application definition and supporting components, but an independent schema installation bundle was not found in a basic DDL scan. A deployment may require manually created tables, views, PL/SQL objects, authorized web credentials, and workspace setup.

For an authorized owner performing a private import:

1. Work in a disposable, access-controlled Oracle APEX workspace.
2. Review export content, credentials and external web-source settings.
3. Provision verified database schema objects separately.
4. Replace API secrets using secured credentials and appropriate roles.
5. Import using APEX App Builder's supported import process and remap application/workspace IDs when required.
6. Perform a manual functional, authorization and data isolation review before publishing or deploying.

These are **preflight recommendations, not evidence of a successful import**.
