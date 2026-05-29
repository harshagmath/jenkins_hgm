from calci.app import add, subtract, multiply, divide

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

def test_subtract():
    assert subtract(5,2) == 3
    assert subtract(0,1) == -1

def test_multiply():
    assert multiply(3,4) == 12
    assert multiply(-1,-5) == 5

def test_divide():
    assert divide(10,2) == 5
    assert divide(3,0) == "Division by 0 is not possible."