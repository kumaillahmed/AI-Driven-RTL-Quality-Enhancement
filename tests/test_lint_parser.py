from rtl_ai.parser.lint_parser import LintParser

def test_parse():
 assert LintParser().parse('WARNING: Test')[0]['severity']=='WARNING'
