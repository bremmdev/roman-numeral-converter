import re


def validate_decimal(input):
    try:
        int(input)
        if int(input) < 1 or int(input) > 3999:
            return False
    except ValueError:
        return False

    return True


def validate_roman(input):
    pattern = re.compile(
        '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
    return bool(re.match(pattern, input))
