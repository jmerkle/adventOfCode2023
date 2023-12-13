from functions_day_13 import *

data_small = read_file_as_list_of_sections('input_small.txt')
data_full = read_file_as_list_of_sections('input.txt')


def test_split_and_compare():
    assert not split_and_compare([1, 1, 2], 0)
    assert split_and_compare([1, 1, 2], 1)


def test_find_middle():
    assert find_middle([1, 1]) == 1
    assert find_middle([1, 2]) == -1
    assert find_middle([1, 1, 2]) == 1
    assert find_middle([2, 1, 1]) == 2
    assert find_middle([2, 1, 1]) == 2
    assert find_middle([1, 2, 2, 2, 1, 1]) == 5


def test_find_multiple_middles():
    assert find_multiple_middles([1, 1]) == [1]
    assert find_multiple_middles([1, 2]) == []
    assert find_multiple_middles([1, 1, 2]) == [1]
    assert find_multiple_middles([2, 1, 1]) == [2]
    assert find_multiple_middles([2, 1, 1]) == [2]
    assert find_multiple_middles([1, 2, 2, 2, 1, 1]) == [5]
    assert find_multiple_middles([1, 1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]


def test_exercise_1():
    assert exercise_1(data_small) == 405


def test_exercise_1_full_data():
    assert exercise_1(data_full) == 27505


def test_smudge_character():
    matrix = np.array([list("#.##..##."), list("..#.##.#.")])
    assert (smudge_character(matrix.copy(), 0) == np.array([list("..##..##."), list("..#.##.#.")])).all()
    assert (smudge_character(matrix.copy(), 1) == np.array([list("####..##."), list("..#.##.#.")])).all()
    assert (smudge_character(matrix.copy(), 8) == np.array([list("#.##..###"), list("..#.##.#.")])).all()
    assert (smudge_character(matrix.copy(), 9) == np.array([list("#.##..##."), list("#.#.##.#.")])).all()
    assert (smudge_character(matrix.copy(), 10) == np.array([list("#.##..##."), list(".##.##.#.")])).all()


def test_manually_process_smudged_pattern():
    matrix1 = np.array([
        list("#.##..##."),
        list("..#.##.#."),
        list("##......#"),
        list("##......#"),
        list("..#.##.#."),
        list("..##..##."),
        list("#.#.##.#."),
            ])

    assert process_matrix(matrix1.copy()) == 5
    assert process_matrix(smudge_character(matrix1.copy(), 0)) == 300

    matrix2 = np.array([
        list("#...##..#"),
        list("#....#..#"),
        list("..##..###"),
        list("#####.##."),
        list("#####.##."),
        list("..##..###"),
        list("#....#..#"),
    ])

    assert process_matrix(matrix2.copy()) == 400
    assert process_matrix(smudge_character(matrix2.copy(), 13)) == 100


def test_process_smudged_pattern():
    pattern1 = [
        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#.",
    ]

    assert process_smudged_pattern(pattern1) == 300

    pattern2 = [
        "#...##..#",
        "#....#..#",
        "..##..###",
        "#####.##.",
        "#####.##.",
        "..##..###",
        "#....#..#",
    ]

    assert process_smudged_pattern(pattern2) == 100

    pattern3 = [
        "..#.#....#....#",
        "..#.#....#....#",
        "..##.#..#..##..",
        "#.#.##.#.#.##.#",
        "####.###.#.##.#",
        ".####.######.##",
        "##.#....#.####.",
        ".####.###.#..#.",
        "#..##...#.#..#.",
    ]

    assert process_smudged_pattern(pattern3) == 12

    pattern4 = [
        "##....##.#.",
        "##.##.#..#.",
        "..####....#",
        "#######..##",
        "##..#......",
        "...##......",
        "###....##..",
        "..#.#..##..",
        "...#.#....#",
        "..##.......",
        "..##.#.##.#",
        "##...##..##",
        "######.##.#",
        "###...#..#.",
        "...###....#",
        "..##.......",
        "###.##....#",
    ]

    assert process_smudged_pattern(pattern4) == 8


def test_exercise_2():
    assert exercise_2(data_small) == 400


def test_exercise_2_full_data():
    assert exercise_2(data_full) == 22906
