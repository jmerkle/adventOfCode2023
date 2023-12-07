from collections import Counter


def read_file_as_list_of_lines_and_filter_empty_lines(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


def hand_type(cards: str) -> int:
    card_frequencies = sorted(Counter(cards).values(), reverse=True)
    if card_frequencies[0] == 5:
        return 6
    if card_frequencies[0] == 4:
        return 5
    if card_frequencies[0] == 3 and card_frequencies[1] == 2:
        return 4
    if card_frequencies[0] == 3:
        return 3
    if card_frequencies[0] == 2 and card_frequencies[1] == 2:
        return 2
    if card_frequencies[0] == 2:
        return 1
    return 0


def with_sortable_chars(card: str) -> str:
    return (card
            .replace("A", "E")
            .replace("K", "D")
            .replace("Q", "C")
            .replace("J", "B")
            .replace("T", "A")
            )


def enumerate_hand(hand: str) -> str:
    [cards, _] = hand.split()
    return str(hand_type(cards)) + with_sortable_chars(cards)


def rank_hands(data: list[str]) -> list[str]:
    return sorted(data, key=enumerate_hand)


def apply_bid(hand_idx: tuple[int, str]) -> int:
    index, hand = hand_idx
    [_, bid] = hand.split()
    return (index + 1) * int(bid)


def exercise_1(data: list[str]) -> int:
    hands_ranked = rank_hands(data)
    winnings = list(map(apply_bid, enumerate(hands_ranked)))
    return sum(winnings)
