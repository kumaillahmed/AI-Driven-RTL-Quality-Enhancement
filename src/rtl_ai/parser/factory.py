from .lint_parser import LintParser
from .cdc_parser import CDCParser
from .rdc_parser import RDCParser

def get_parser(kind):
    return {'lint':LintParser(),'cdc':CDCParser(),'rdc':RDCParser()}[kind]
