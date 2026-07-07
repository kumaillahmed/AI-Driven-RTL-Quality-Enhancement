from .base_parser import BaseParser
class RDCParser(BaseParser):
    def parse(self,text):
        return [{'type':'RDC','raw':l} for l in text.splitlines() if l.strip()]
