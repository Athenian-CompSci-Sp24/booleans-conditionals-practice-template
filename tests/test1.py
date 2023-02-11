import src.fix_code_1


def test_inc():
    assert "Password accepted!" == src.fix_code_1.password("p@sSwoRd!")
    assert "Invalid password - goodbye." == src.fix_code_1.password("password")
