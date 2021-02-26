from collatz import next_collatz_element

def test_next_collatz_element_1():
    assert next_collatz_element(4) == 2

def test_next_collatz_element_2():
    assert next_collatz_element(5) == 16