import unittest

import app

def test_test():
    assert app.test() == "Works!"


def test_calculator():
    res=app.calculator(12)
    assert res[0]==True
        
        
