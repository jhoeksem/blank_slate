from fns import *

def test_inc():
    assert inc(3) == 4
    assert inc(5.5) == 6.5

def test_greet():
    assert greet("John") == "Hello John!"
    assert greet("") == "Hello !"

def test_square():
    assert square(5) == 25
    assert square(2.5) == 6.25

def test_dec():
    assert dec(3) == 1
    assert dec(5.5) == 3
