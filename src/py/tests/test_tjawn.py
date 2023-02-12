import pytest

import tjawn

def test_example():
    t = '''
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
    '''
    r = tjawn.loads(t)
    assert r == {
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

def test_snippet_a():
    t = '''
    '''
    r = tjawn.loads(t)
    assert r == { }

def test_snippet_b():
    t = ''
    r = tjawn.loads(t)
    assert r == { }

def test_snippet_0():
    t = '''
    a: 1
    b = 2
    '''
    r = tjawn.loads(t)
    assert r == { 'a': 1, 'b': 2 }

def test_snippet_1():
    t = '''
a: null
b: nULl
c: true
d: FALSE
    '''
    r = tjawn.loads(t)
    assert r == { 'a': None, 'b': None, 'c': True, 'd': False }

def test_snippet_2():
    t = '''
    a = 1
    b = 2.0
    c = 3.7e9
    '''
    r = tjawn.loads(t)
    assert r == { 'a': 1, 'b': 2, 'c': 3700000000 }

def test_snippet_3():
    t = '''
a: "my string"
b: 'my other string'
c: 'a string with
a linebreak'

d: aBareString
e: a-bare-string

f: https://example.com
g: http://example.com
    '''
    r = tjawn.loads(t)
    assert r == {
        'a': 'my string',
        'b': 'my other string',
        'c': 'a string with\na linebreak',
        'd': 'aBareString',
        'e': 'a-bare-string',
        'f': 'https://example.com',
        'g': 'http://example.com',
    }

def test_snippet_4():
    t = '''
a: """
        # Example

        This text looks very nice in the config file.
          * And the indentations are preserved!
            Which is super awesome
"""
    '''
    r = tjawn.loads(t)
    assert r == {
        'a': "# Example\n\nThis text looks very nice in the config file.\n  * And the indentations are preserved!\n    Which is super awesome"
    }

def test_snippet_5():
    t = '''
a = [ 1 2 3 4 5, 6, 7, 8,]
b = [ True "banana" { c: "orange" }]
c = [x, y, [1 2 3]]
    '''
    r = tjawn.loads(t)
    assert r == {
        'a': [ 1, 2, 3, 4, 5, 6, 7, 8 ],
        'b': [ True, "banana", { 'c': "orange" } ],
        'c': [ 'x', 'y', [1, 2, 3]],
    }

def test_snippet_6():
    t = '''
a: { "bananas" "oranges" "pears" }
b: { "bananas" "oranges" "pears" "bananas" }
c: { _ }
    '''
    r = tjawn.loads(t)
    assert r == {
        'a': { "bananas", "oranges", "pears" },
        'b': { "bananas", "oranges", "pears" },
        'c': set()
    }

def test_snippet_7():
    t = '''
a: { x: 1, y: 2}
b: { 'alpha': 3 beta=4 zeta:{a=1, y=2}}
c: {}
    '''
    r = tjawn.loads(t)
    assert r == {
        'a': { 'x': 1, 'y': 2},
        'b': { 'alpha': 3, 'beta': 4, 'zeta': { 'a': 1, 'y':2}},
        'c': dict()
    }
