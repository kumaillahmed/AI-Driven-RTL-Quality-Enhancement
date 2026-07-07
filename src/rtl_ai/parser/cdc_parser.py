from .base_parser import BaseParser
class CDCParser(BaseParser):
    def parse(self,text):
        return [{'type':'CDC','raw':l} for l in text.splitlines() if l.strip()]
