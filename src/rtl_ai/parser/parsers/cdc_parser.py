from rtl_ai.parser.interfaces.base_parser import BaseParser

class CDCParser(BaseParser):
    def parse(self, text:str):
        return [l for l in text.splitlines() if l.startswith("CDC")]
