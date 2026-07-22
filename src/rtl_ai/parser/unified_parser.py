from rtl_ai.parser.factory import get_parser

class UnifiedParser:
    def parse(self, parser_type:str, text:str):
        return get_parser(parser_type).parse(text)
