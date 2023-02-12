from collections import namedtuple

from .lark_parser import Lark_StandAlone, Transformer

class TJawnTransformer(Transformer):
    Pair = namedtuple('Pair', ['k', 'v'])

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

    def number(self, n):
        (n,) = n
        return float(n)

    def string(self, s):
        (s,) = s
        if s[0] == '"':
            s = str(s[1:-1]).replace('\\"', '"')
        elif s[0] == "'":
            s = str(s[1:-1]).replace("\\'", "'")
        else:
            s = str(s)
        return s

    def text(self, s):
        (s,) = s
        if s[0] == '"':
            s = str(s[3:-3]).replace('\\"', '"')
        elif s[0] == "'":
            s = str(s[3:-3]).replace("\\'", "'")
        else:
            s = str(s)

        lines = s.split("\n")

        while len(lines) > 0 and (not lines[0] or lines[0].isspace()):
            del lines[0]

        while len(lines) > 0 and (not lines[len(lines)-1] or lines[len(lines)-1].isspace()):
            del lines[len(lines)-1]

        i = 0
        while i < len(lines[0]) and lines[0][i].isspace():
            i += 1
        prefix = lines[0][:i]

        res = []
        for l in lines:
            res.append(l.removeprefix(prefix))

        return '\n'.join(res)

    def list(self, s):
        if len(s) == 1 and s[0] is None:
            return list()
        return list(s)

    def set(self, s):
        if len(s) == 1 and s[0] is None:
            return set()
        return set(s)

    def dict(self, s):
        if len(s) == 1 and s[0] is None:
            return dict()
        return {p.k: p.v for p in s}

    def file(self, s):
        return self.dict(s)

    def key(self, s):
        (s, ) = s
        if s.type == 'BARE_STR':
            k = str(s)
        elif s[0] == '"':
            k = str(s[1:-1]).replace('\\"', '"')
        else:
            k = str(s[1:-1]).replace("\\'", "'")
        return k

    def pair(self, s):
        return self.Pair(s[0], s[1])

parser = Lark_StandAlone(transformer=TJawnTransformer())

def loads(text: str):
    return parser.parse(text)
