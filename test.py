print(" hello in cloud world -1")

from fibbonacci import sum, sum_only_positive

#def test_fib_1_equals_1():
 #   assert fibbo(2)== 5

#def test_fib_2_equals_1():
 #   assert fibbo(3) == 21

#def test_fib_6_equals_8():
    #assert fibbo(4) == 89
    
def test_sum():
    assert sum(5, 5) == 10


#def test_sum():
  #  assert sum(-5, 2) == -3

def test_sum_positive_ok():
    assert sum_only_positive(2, 2) == 4

def test_sum_positive_fail():
    assert sum_only_positive(-1, 2) is None

