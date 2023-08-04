from convert_number import convert_decimal, convert_roman

# test sets, these tests are used for both conversion methods
test_regular = [(1, "I"), (13, "XIII"), (27, "XXVII"),
                (581, "DLXXXI"), (1231, "MCCXXXI")]

test_fours = [(4, "IV"), (24, "XXIV"), (384, "CCCLXXXIV"),
              (444, "CDXLIV"), (3424, "MMMCDXXIV")]

test_nines = [(9, "IX"), (49, "XLIX"), (99, "XCIX"),
              (2559, "MMDLIX"), (3999, "MMMCMXCIX")]


def test_convert_decimal():
    for input, output in test_regular:
        assert convert_decimal(input) == output


def test_convert_decimal_with_fours():
    for input, output in test_fours:
        assert convert_decimal(input) == output


def test_convert_decimal_with_nines():
    for input, output in test_nines:
        assert convert_decimal(input) == output


def test_convert_roman():
    for input, output in test_regular:
        assert convert_roman(output) == input


def test_onvert_roman_with_fours():
    for input, output in test_fours:
        assert convert_roman(output) == input


def test_convert_roman_with_nines():
    for input, output in test_nines:
        assert convert_roman(output) == input
