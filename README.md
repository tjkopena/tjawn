# tjawn <img src="https://github.com/tjkopena/tjawn/raw/main/docs/shark.png" height="50" title="tjawn" alt='Drawing of a shark thrusting out of the water and growling "Rwaa rwaa, rwaa rwaa!" as it tries to eat you.' style="vertical-align: middle" />

This is an implementation of *jawns*, a human friendly lightweight
object notation.  A jawn is a Python dict literal or a slight superset
of JSON but with more flexible formatting. An example:

```
protocol: 1.0,
token: 854c37ee-517c-4ba6-b56b-06475ad24041
conn: {
    offer= { 'TLS1.2', TLS1.3  "TLS 1.17" }
    "dns:resolver" = 10.0.0.1
    cert: """
        -----BEGIN CERTIFICATE-----
        MIICUTCCAfugAwIBAgIBADANBgkqhkiG9w0BAQQFADBXMQswCQYDVQQGEwJDTjEL
        MAkGA1UECBMCUE4xCzAJBgNVBAcTAkNOMQswCQYDVQQKEwJPTjELMAkGA1UECxMC
        VU4xFDASBgNVBAMTC0hlcm9uZyBZYW5nMB4XDTA1MDcxNTIxMTk0N1oXDTA1MDgx
            ...
    """
}
```

Which parses to the equivalent of this Python literal:
```python
{
    "protocol": 1.0,
    "token": "854c37ee-517c-4ba6-b56b-06475ad24041",
    "conn": {
        "offer": {"TLS1.2", "TLS1.3",  "TLS 1.17"},
        "dns:resolver": "10.0.0.1",
        "cert": """-----BEGIN CERTIFICATE-----
MIICUTCCAfugAwIBAgIBADANBgkqhkiG9w0BAQQFADBXMQswCQYDVQQGEwJDTjEL
MAkGA1UECBMCUE4xCzAJBgNVBAcTAkNOMQswCQYDVQQKEwJPTjELMAkGA1UECxMC
VU4xFDASBgNVBAMTC0hlcm9uZyBZYW5nMB4XDTA1MDcxNTIxMTk0N1oXDTA1MDgx
    ..."""
    }
}
```

Some features to call out:
* Identifier-styled strings do not need to be quoted (for both keys & values).
* Single or double quotes can be used interchangeably (in matched pairs).
* Multi-line text _can_ have whitespace stripped while preserving relative indentation.
* Key/value pairs are denoted by either ':' or '=' as you wish.
* Commas are largely optional but permitted (i.e., allowed on closing elements).
* Objects, sets, and lists are delimited by brackets, not whitespace.
* Sets are supported.

> _"jawn?"_

JSON Alternative Written Notation?\
Joe's Awesome Wacky ... Notation?\
[Don't think about it too hard.](https://en.wikipedia.org/wiki/Jawn)


> _"But why?"_

I (tjkopena) find it _almost_ convenient to write simple config files
or parameter sets and so on in JSON.  I don't implement such often
enough to bother to remember how to format TOML or YAML or whateverML,
and in any event I dislike their whitespace-based formatting, nesting,
and other aspects.  I know JSON, use it all the time, I just want to
write a little object file in it.  But it's _not actually_ convenient
to do so because JSON is a picky, pedantic pain in the ass---double
quotes on everything, no trailing commas, blah blah blah GTFO. Hence
jawns, a similarly simple, straightforward object model and syntax
that's not too fussed about the details.


## jawns

Quick outline of jawns as I'm getting tired of writing these notes---

A jawn is a mapping (dictionary) of zero or more key/value pairs.\
Key/value pair elements are separated by colons or equals.\
Key/value pairs can be separated by commas or not, and a trailing comma is permitted.
```
a: 1
b = 2
```

Keys are strings (quoted or bare, see below).

Values are null, true, false, numbers, strings, texts, lists, sets, or nested jawns.

Null, true, and false are case-insensitive.
```
a: null
b: nULl
c: true
d: FALSE
```

Numbers are signed floats in decimal or exponential notation.
```
a = 1
b = 2.0
c = 3.7e9
```

Strings consist of quoted strings, bare strings, or http/https URLs.\
Quoted strings are denoted by matched double or single quotes and permit linebreaks.\
Bare strings are a sequence of characters excluding whitespace, quotes, brackets, colons, equals, or commas.
```
a: "my string"
b: 'my string'
c: 'a string with
a linebreak'

d: aBareString
e: a-bare-string

f: https://example.com
g: http://example.com
```

Texts are denoted by matched pair of quote triplets (single or double) and permit linebreaks.\
Lines consisting only of whitespace are removed from the start and end of texts.\
Any whitespace at the start of the first non-whitespace line is taken as a prefix and removed from the start of all lines.
```
a: """
        # Example

        This text looks very nice in the config file.
          * And the indentations are preserved!
            Which is super awesome
"""
```

Lists are denoted by zero or more values within square brackets.\
The values can be separated by commas or not, and a trailing comma is permitted.
```
a = [ 1 2 3 4 5, 6, 7, 8,]
b = [ True "banana" { c: "orange" }]
c = [x, y, [1 2 3]]
```

Sets are denoted by one or more values within curly brackets, or a single underscore for empty set.\
It is legal to include multiple equivalent values in the set, but these are collapsed in parsing.\
The values can be separated by commas or not, and a trailing comma is permitted.
```
a: { "bananas" "oranges" "pears" }
b: { "bananas" "oranges" "pears" "bananas" }
c: { _ }
```

Nested jawns are delimited by curly brackets.
```
a: { x: 1, y: 2}
b: { 'alpha': 3 beta=4 zeta:{a=1, y=2}}
c: {}
```

A grammar for jawns in Lark is [in the `src` folder](src/jawn.g).

## Implementations

Currently tjawn has a Python implementation of jawns. JavaScript
implementation is expected in the near future.

### Python

#### Setup

tjawn's Python module has no dependencies.  It is [listed in
PyPi](https://pypi.org/project/tjawn/) and should be includable in
all the usual ways.

#### Usage

```
import tjawn

o = tjawn.loads('a: "Four score and seven..."')
print(tjawn.dumps(o))
```

#### Development Notes

Internally, tjawn's Python module is implemented using Lark to
generate the lexer and parser, which are then vendored in the project
rather than incurring a dependency.  To generate both these:

```bash
python -m lark.tools.standalone src/jawn.g > src/py/tjawn/lark_parser.py
```

Tests can be run from the `src/py` directory via `pytest`.


## License

tjawn is released under MIT-0:

> Copyright 2023 tjkopena
>
> Permission is hereby granted, free of charge, to any person
> obtaining a copy of this software and associated documentation files
> (the "Software"), to deal in the Software without restriction,
> including without limitation the rights to use, copy, modify, merge,
> publish, distribute, sublicense, and/or sell copies of the Software,
> and to permit persons to whom the Software is furnished to do so.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
> EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
> MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
> NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
> BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
> ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
> CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

[Shark icon](https://thenounproject.com/icon/shark-1257563/) by Luis Prado for The Noun Project, CCBY3.0.
