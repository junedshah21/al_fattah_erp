import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_public_release.py"
spec = importlib.util.spec_from_file_location("guard", SCRIPT)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class ReleaseGuardTest(unittest.TestCase):
    def test_safe_docs(self):
        with TemporaryDirectory() as d:
            f = Path(d) / "README.md"
            f.write_text("A demo using Oracle APEX.")
            self.assertEqual(guard.scan(Path(d)), [])

    def test_zip_rejected(self):
        with TemporaryDirectory() as d:
            f = Path(d) / "export.zip"
            f.write_bytes(b"PK")
            self.assertIn("unreviewed_export_or_archive", [x[1] for x in guard.scan(Path(d))])

    def test_apex_export_rejected(self):
        with TemporaryDirectory() as d:
            f = Path(d) / "f238769.sql"
            f.write_text("prompt app")
            self.assertEqual(guard.scan(f)[0][1], "unreviewed_export_or_archive")

    def test_openai_shape_rejected(self):
        with TemporaryDirectory() as d:
            f = Path(d) / "code.sql"
            f.write_text("p_key=>'sk-proj-" + "x" * 38 + "'")
            self.assertIn("openai_key", [x[1] for x in guard.scan(f)])

    def test_rapidapi_shape_rejected(self):
        with TemporaryDirectory() as d:
            f = Path(d) / "code.sql"
            f.write_text("p_name=>'x-rapidapi" + "-key', p_value=>'" + "x" * 32 + "'")
            self.assertIn("rapidapi_inline_header", [x[1] for x in guard.scan(f)])

    def test_no_secret_echo(self):
        with TemporaryDirectory() as d:
            f = Path(d) / "source.sql"
            secret = "sk-proj-" + "z" * 38
            f.write_text(secret)
            summary = "\n".join(f"{p}: {reason}" for p, reason in guard.scan(f))
            self.assertNotIn(secret, summary)

    def test_unconditional_admin_auth_rejected(self):
        with TemporaryDirectory() as d:
            f = Path(d) / "sanitized_apex.sql"
            f.write_text("wwv_flow_imp_shared.create_security_scheme(\n"
                         " p_name=>'Administration Rights'\n"
                         ",p_scheme_type=>'NATIVE_FUNCTION_BODY'\n"
                         ",p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(\n"
                         "  'plsql_function_body', 'return true;')).to_clob\n"
                         ");")
            self.assertIn("apex_unconditional_admin_access", [x[1] for x in guard.scan(f)])

    def test_authorization_not_flagged_when_false(self):
        with TemporaryDirectory() as d:
            f = Path(d) / "sanitized_apex.sql"
            f.write_text("wwv_flow_imp_shared.create_security_scheme(\n"
                         " p_name=>'Administration Rights'\n"
                         ",p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(\n"
                         " 'plsql_function_body', 'return false;')).to_clob);")
            self.assertNotIn("apex_unconditional_admin_access", [x[1] for x in guard.scan(f)])

    def test_rapidapi_multiline_apex_export(self):
        with TemporaryDirectory() as d:
            f = Path(d) / "review.sql"
            f.write_text(" p_name=>'x-rapidapi-key'\n"
                         ",p_static_id=>'x-rapidapi-key'\n"
                         ",p_param_type=>'HEADER'\n"
                         ",p_data_type=>'VARCHAR2'\n"
                         ",p_default_value_type=>'STATIC'\n"
                         ",p_value=>'" + "a" * 32 + "'\n")
            self.assertIn("rapidapi_inline_header", [x[1] for x in guard.scan(f)])

    def test_rapidapi_without_value_not_flagged(self):
        with TemporaryDirectory() as d:
            f = Path(d) / "review.sql"
            f.write_text(" p_name=>'x-rapidapi-key'\n,p_param_type=>'HEADER'\n")
            self.assertNotIn("rapidapi_inline_header", [x[1] for x in guard.scan(f)])

    def test_missing_path_error(self):
        self.assertEqual(guard.main(["/path/not/really/present/erp-check"]), 2)

    def test_oversize_detection(self):
        with TemporaryDirectory() as d:
            f = Path(d) / "huge.txt"
            with f.open("wb") as out:
                out.truncate(guard.MAX_BYTES + 1)
            self.assertEqual(guard.scan(f)[0][1], "file_too_large_to_scan")


if __name__ == "__main__":
    unittest.main()
