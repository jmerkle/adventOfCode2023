import re
import queue


def read_file_as_list_of_lines_and_filter_empty_lines(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


def exercise_1(data):
    points = [calculate_points_for_card(card) for card in data]
    return sum(points)


def calculate_points_for_card(card):
    [winning_numbers, card_numbers] = parse_card(card)
    numbers_in_both_lists = set(winning_numbers) & set(card_numbers)
    if len(numbers_in_both_lists) < 1:
        return 0
    return 2 ** (len(numbers_in_both_lists) - 1)


def parse_card(card):
    [winning_string, card_string] = card.split(":")[1].split("|")
    return [extract_numbers(winning_string), extract_numbers(card_string)]


def extract_numbers(text):
    return [int(n) for n in re.findall(r'\d+', text)]


def exercise_2(data):
    wins_per_card = calculate_wins_for_all_cards(data)
    card_count = 0
    card_queue = queue.Queue()
    [card_queue.put(c) for c in range(0, len(data))]
    while card_queue.qsize() > 0:
        card = card_queue.get()
        card_count += 1
        additional_cards = wins_per_card[card]
        if additional_cards > 0:
            [card_queue.put(c) for c in range(card+1, card+1+additional_cards)]
    return card_count


def calculate_wins_for_all_cards(data):
    return [calculate_wins_for_single_card(card) for card in data]


def calculate_wins_for_single_card(card):
    [winning_numbers, card_numbers] = parse_card(card)
    numbers_in_both_lists = set(winning_numbers) & set(card_numbers)
    return len(numbers_in_both_lists)
