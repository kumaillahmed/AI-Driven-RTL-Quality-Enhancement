import re
from .base_parser import BaseParser
class LintParser(BaseParser):
    pat=re.compile(r'^(ERROR|WARNING):\s*(.*)$')
    def parse(self,text):
        out=[]
        for l in text.splitlines():
            m=self.pat.match(l.strip())
            if m: out.append({'severity':m.group(1),'message':m.group(2)})
        return out
