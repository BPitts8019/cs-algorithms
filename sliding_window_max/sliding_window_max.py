'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def max_of(arr):
    if len(arr) == 1:
        return arr[0]

    max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]

    return max_num


def sliding_window_max(nums, k):
    max_nums = []

    num_iterations = len(nums) - k + 1
    for i in range(num_iterations):
        window = nums[i:i+k]
        max_nums.append(max_of(window))
    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
