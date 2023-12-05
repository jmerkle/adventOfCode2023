from functions_day_5 import *
from multiprocessing import freeze_support


data_full = read_file_as_list_of_sections('input.txt')
data_small = read_file_as_list_of_sections('input_small.txt')

if __name__ == '__main__':
    freeze_support()
    result = exercise_2_parallel(data_full, 1000000)
    print(result)
