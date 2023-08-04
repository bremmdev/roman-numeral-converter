def convert_decimal(input):
    roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    decimal = [1000, 500, 100, 50, 10, 5, 1]
    result = ""
    idx = 0
    n = input

    # count the number of occurrences of each roman number
    cnt = []
    for d in decimal:
        c = n // d
        n = n - (c * d)
        cnt.append(c)

    for c in cnt:

        not_last = idx < (len(roman) - 1)

        # detect a 9
        if not_last and c == 1 and cnt[idx + 1] == 4:
            cnt[idx + 1] = 0
            result += roman[idx + 1] + roman[idx - 1]

        # detect a 4
        elif not_last and c == 0 and cnt[idx + 1] == 4:
            cnt[idx + 1] = 0
            result += roman[idx + 1] + roman[idx]

        elif c > 0:
            result += c * roman[idx]

        idx += 1

    return result


def convert_roman(input):
    convert_map = {'M': 1000, 'D': 500, 'C': 100,
                   'L': 50, 'X': 10, 'V': 5, 'I': 1}
    exceptions = [('CM', 900), ('CD', 400), ('XC', 90),
                  ('XL', 40), ('IX', 9), ('IV', 4)]
    exceptions_sum = 0
    sum = 0
    idx = 0
    n = input

    # count the sum of the exceptions
    for key, val in exceptions:
        if key in input:
            exceptions_sum += val
            n = n.replace(key, "")

    # count the remaining values
    for r in n:
        sum += convert_map[r]

    return sum + exceptions_sum
