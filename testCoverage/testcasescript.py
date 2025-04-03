import oddEven

def checkeven():
    assert oddEven.check_even_odd(2) == "Even"
def checkodd():
    assert oddEven.check_even_odd(3) == "Odd"
def checkzero():
    assert oddEven.check_even_odd(0) == "Even"
def checknegative():
    assert oddEven.check_even_odd(-3) == "Odd"
def checknegativeeven():
    assert oddEven.check_even_odd(-4) == "Even"
