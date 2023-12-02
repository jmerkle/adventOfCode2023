def find_digits(text):
    return [c for c in text if c.isdigit()]


def concat_first_and_last_digit_to_int(text):
    digits = find_digits(text)
    if len(digits) > 0:
        return int(digits[0] + digits[-1])
    else:
        return 0


f = open('input.txt', 'r')
data = f.read()
f.close()
lines = data.split('\n')
# numbers = map(lambda line: line)
for line in lines:
    print(line)
    print(concat_first_and_last_digit_to_int(line))

sumOfNumber = sum(map(lambda line: concat_first_and_last_digit_to_int(line), lines))
print(sumOfNumber)
