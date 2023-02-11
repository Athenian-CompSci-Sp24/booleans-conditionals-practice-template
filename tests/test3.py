import src.fix_code_2


def test_write_code_2():
    assert "even" == src.fix_code_2.even_odd(10)
    assert "odd" == src.fix_code_2.even_odd(3)
    assert "odd" == src.fix_code_2.even_odd(15)
    assert "even" == src.fix_code_2.even_odd(100)
