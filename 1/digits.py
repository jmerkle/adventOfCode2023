def find_digits(text):
    return [c for c in text if c.isdigit()]

def replace_spelled_out_digits_with_numeral(text):
    return (text
            .replace("one", "1")
            .replace("two", "2")
            .replace("three", "3")
            .replace("four", "4")
            .replace("five", "5")
            .replace("six", "6")
            .replace("seven", "7")
            .replace("eight", "8")
            .replace("nine", "9")
            )

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
    print("##########")
    print(line)
    print(concat_first_and_last_digit_to_int(line))
    print(replace_spelled_out_digits_with_numeral(line))
    print(concat_first_and_last_digit_to_int(replace_spelled_out_digits_with_numeral(line)))

exercise1 = sum(map(lambda line: concat_first_and_last_digit_to_int(line), lines))

lines_with_replaced_spelled_out_digits = list(map(lambda line: replace_spelled_out_digits_with_numeral(line), lines))
exercise2 = sum(map(lambda line: concat_first_and_last_digit_to_int(line), lines_with_replaced_spelled_out_digits))

print("Result for exercise 1")
print(exercise1)
print("Result for exercise 2")
print(exercise2)
