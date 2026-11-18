# Security advisory and disclosure policy

## Immediate action required

A static review of the Oracle APEX export `f238769.sql` identified **two inline OpenAI API-key occurrences and one RapidAPI key**. The ZIP presently published in the public GitHub repository has **not been byte-for-byte inspected here**, so whether that specific ZIP contains the same credentials remains unverified. Treat any matching API credentials as exposed.

1. **Revoke / rotate** affected OpenAI and RapidAPI keys using their providers' consoles. Do not reuse old values.
2. Update the live APEX application's references to use appropriately protected server-side **APEX Web Credentials** or secret management; remove hard-coded secrets from pages, processes and web-source parameters.
3. Check provider usage and billing logs for unexpected charges.
4. Remove the original archive from the public branch after safe replacement, and follow GitHub's guidance to remove sensitive data from history. **A normal delete/commit does not erase old Git objects or forks.**
5. Check embedded static assets, personal data and third-party redistribution rights before publishing a sanitized source export.

Do **not** post credential values in public issues or pull requests. Report suspected security problems privately to the repository owner.

A redacted export is for review only; a successful pattern replacement is **not** evidence of complete secret removal or import readiness.
