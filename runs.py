"""
Script for finding consecutive runs of three in a list.
"""


def find_consecutive_runs(num_list):
    """
    To check if n elements in an array are consecutive, we can use:
    max(visited_array) - min(visited_array) + 1 == n && len(distinct elements in array) == n. We'll place
    the temp array/list in a set to check distinctness of members. I think this has a time complexity of O(n)?
    If we wanted, we could extend this by setting the run length as a parameter in the function.

    :param num_list: list[int]
    :return found_idx: list[int]
    """
    found_idx = []
    for i in range(len(num_list) - 1):
        temp_list = num_list[i:i+3]
        if max(temp_list) - min(temp_list) + 1 == 3 and len(set(temp_list)) == 3:
            found_idx.append(i)

    if len(found_idx):
        return found_idx


def main():
    test_list_1 = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
    test_list_2 = [1, 2, 3, 4, 5, 6, 5, 4]
    test_no_runs = [1, 2, 5]
    test_1_known_idx = [0, 4, 6, 7]
    test_2_known_idx = [0, 1, 2, 3, 5]

    found_runs_1 = find_consecutive_runs(test_list_1)
    found_runs_2 = find_consecutive_runs(test_list_2)
    no_found_runs = find_consecutive_runs(test_no_runs)

    assert found_runs_1 == test_1_known_idx
    assert found_runs_2 == test_2_known_idx
    assert no_found_runs is None

if __name__ == "__main__":
    main()
