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

def extract_numbers(text):
    if len(text) < 1: return ""
    #if text[0:0].isdigit(): return text[0:0] + string_starts_with_numeral(text[1:])
    if text.startswith("1"): return "1" + extract_numbers(text[1:])
    if text.startswith("2"): return "2" + extract_numbers(text[1:])
    if text.startswith("3"): return "3" + extract_numbers(text[1:])
    if text.startswith("4"): return "4" + extract_numbers(text[1:])
    if text.startswith("5"): return "5" + extract_numbers(text[1:])
    if text.startswith("6"): return "6" + extract_numbers(text[1:])
    if text.startswith("7"): return "7" + extract_numbers(text[1:])
    if text.startswith("8"): return "8" + extract_numbers(text[1:])
    if text.startswith("9"): return "9" + extract_numbers(text[1:])
    if text.startswith("one"): return "1" + extract_numbers(text[1:])
    if text.startswith("two"): return "2" + extract_numbers(text[1:])
    if text.startswith("three"): return "3" + extract_numbers(text[1:])
    if text.startswith("four"): return "4" + extract_numbers(text[1:])
    if text.startswith("five"): return "5" + extract_numbers(text[1:])
    if text.startswith("six"): return "6" + extract_numbers(text[1:])
    if text.startswith("seven"): return "7" + extract_numbers(text[1:])
    if text.startswith("eight"): return "8" + extract_numbers(text[1:])
    if text.startswith("nine"): return "9" + extract_numbers(text[1:])
    return extract_numbers(text[1:])

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
    print(extract_numbers(line))
    print(concat_first_and_last_digit_to_int(extract_numbers(line)))

exercise1 = sum(map(lambda line: concat_first_and_last_digit_to_int(line), lines))

extracted_numbers = list(map(lambda line: extract_numbers(line), lines))
combined_numbers = list(map(lambda line: concat_first_and_last_digit_to_int(line), extracted_numbers))
exercise2 = sum(combined_numbers)

print("Result for exercise 1")
print(exercise1)
print("Result for exercise 2")
print(exercise2)

