from rtl_ai.parser.parsers.lint_parser import LINTParser
from rtl_ai.parser.parsers.cdc_parser import CDCParser
from rtl_ai.parser.parsers.rdc_parser import RDCParser

def get_parser(kind:str):
    kind=kind.lower()
    return {"lint":LINTParser(),"cdc":CDCParser(),"rdc":RDCParser()}[kind]
