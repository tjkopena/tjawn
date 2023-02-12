import pytest

import tjawn

def test_null_0():
    r = tjawn.loads(
        'a: null'
        )
    assert r == { 'a': None }

def test_null_1():
    r = tjawn.loads(
        'a: nULL'
        )
    assert r == { 'a': None }

def test_null_2():
    r = tjawn.loads(
        'a: NULL'
        )
    assert r == { 'a': None }

def test_true_0():
    r = tjawn.loads(
        'a: true'
        )
    assert r == { 'a': True }

def test_true_1():
    r = tjawn.loads(
        'a: TRUE'
        )
    assert r == { 'a': True }

def test_true_2():
    r = tjawn.loads(
        'a: tRUe'
        )
    assert r == { 'a': True }

def test_false_0():
    r = tjawn.loads(
        'a: false'
        )
    assert r == { 'a': False }

def test_false_1():
    r = tjawn.loads(
        'a: False'
        )
    assert r == { 'a': False }

def test_false_2():
    r = tjawn.loads(
        'a: FALSE'
        )
    assert r == { 'a': False }

def test_number_0():
    r = tjawn.loads(
        'a: 4'
        )
    assert r == { 'a': 4 }

def test_number_1():
    r = tjawn.loads(
        'a: 7.0'
        )
    assert r == { 'a': 7.0 }

def test_number_2():
    r = tjawn.loads(
        'a: 4,'
        )
    assert r == { 'a': 4 }

def test_number_3():
    r = tjawn.loads(
        'a: 7.0\n'
        )
    assert r == { 'a': 7.0 }

def test_number_4():
    r = tjawn.loads(
        'a: 4  b: 8'
        )
    assert r == { 'a': 4 , 'b': 8}

def test_number_5():
    r = tjawn.loads(
        'a: 4  b:8'
        )
    assert r == { 'a': 4 , 'b': 8}

def test_number_6():
    r = tjawn.loads(
        'a: 4,b:8'
        )
    assert r == { 'a': 4 , 'b': 8}

def test_barestr_0():
    r = tjawn.loads(
        'a: 10.0.0.1'
        )
    assert r == { 'a': '10.0.0.1' }

def test_barestr_set_0():
    r = tjawn.loads(
        'a: {10.0.0.1, 127.0.0.1}'
        )
    assert r == { 'a': {'10.0.0.1', '127.0.0.1'} }

def test_barestr_key_0():
    r = tjawn.loads(
        '1.0: 4'
        )
    assert r == { '1.0': 4 }

def test_quotstr_key_0():
    r = tjawn.loads(
        '"key with a space": 4'
        )
    assert r == { 'key with a space': 4 }

def test_quotstr_key_1():
    r = tjawn.loads(
        '"colon:key": 4'
        )
    assert r == { 'colon:key': 4 }

def test_barestr_value_0():
    r = tjawn.loads(
        'k1: "abcd:123"'
        )
    assert r == { 'k1': 'abcd:123' }
