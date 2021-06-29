from Calculate.calc import calculator


def test_addition():
    assert calculator.sum(1,2) == 3
    assert calculator.sum(1,0) == 1
    assert calculator.sum(1,-1) == 0


def test_subtract():
    assert calculator.subtract(1,2) == -1
    assert calculator.subtract(1,0) == 1
    assert calculator.subtract(1,-1) == 2


def test_multiply():
    assert calculator.multiply(1,2) == 2
    assert calculator.multiply(1,0) == 0
    assert calculator.multiply(1,-1) == -1


def test_divide():
    assert calculator.divide(1,2) == 0.5
    assert calculator.divide(0,1) == 0
    assert calculator.divide(1,-1) == -1