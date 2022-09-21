from factorial import *
def test_factorial():
    assert factorial(5) == 120
def test_logFatorial():
    assert factorial(5) == round(math.exp(logFactorial(5)))