def _quote_escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')

def _serialize(o, prefix, indent, eoln):

    pf = prefix+indent
    s = ""

    if o is None:
        s = "null"

    elif isinstance(o, bool):
        s = "true" if o else "false"

    elif isinstance(o, (int, float)):
        s = str(o)

    elif isinstance(o, str):
        s = f'"{_quote_escape(o)}"'

    elif isinstance(o, list):
        s = "[" + eoln
        comma = ""
        for v in o:
            s = s + comma + pf
            s += _serialize(v, pf+indent, indent, eoln)
            comma = "," + eoln
        s = s + eoln + prefix + "]"

    elif isinstance(o, set):
        s = "{" + eoln
        comma = ""
        for v in o:
            s = s + comma + pf
            s += _serialize(v, pf+indent, indent, eoln)
            comma = "," + eoln
        s = s + eoln + prefix + "}"

    elif isinstance(o, dict):
        s = "{" + eoln
        comma = ""
        for k,v in o.items():
            s = s + comma + pf
            esc = _quote_escape(k)
            s += (f'"{esc}"' if ' ' in esc else esc) + ": "
            s += _serialize(v, pf+indent, indent, eoln)
            comma = "," + eoln
        s = s + eoln + prefix + "}"

    return s

def dumps(o, indent="  ", eoln="\n"):
    return _serialize(o, "", indent, eoln)
