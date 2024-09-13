import random
import time

from insertion_sort.sort import insertion_sort

N = 100
random.seed(int(time.time()))

# Do not change the following lines
def test_insertion_sort():
    input_list = list(range(N))
    random.shuffle(input_list)
    output_list = insertion_sort(input_list)
    assert output_list == sorted(output_list), "Input list is not sorted"
    print("Test passed!")


def test_reference():
    input_list = list(range(N))
    random.shuffle(input_list)
    output_list = sorted(input_list)
    assert output_list == sorted(output_list), "Input list is not sorted"
    print("Test passed!")