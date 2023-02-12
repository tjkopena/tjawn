import pytest

import tjawn

def test_text_0():
    r = tjawn.loads("""
a: "This is a multiline string
    that will not adjust spacing."
        """)
    assert r == { 'a': "This is a multiline string\n    that will not adjust spacing." }

def test_text_1():
    r = tjawn.loads('''
a: 'This is a multiline string
    that will not adjust spacing.'
        ''')
    assert r == { 'a': "This is a multiline string\n    that will not adjust spacing." }
