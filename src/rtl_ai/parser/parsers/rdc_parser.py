from rtl_ai.parser.interfaces.base_parser import BaseParser

class RDCParser(BaseParser):
    def parse(self, text:str):
        return [l for l in text.splitlines() if l.startswith("RDC")]
