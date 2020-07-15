'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    rtn_arr = arr
    temp_num = None
    move_idx = 0
    for (index, number) in enumerate(arr):
        if number != 0:
            temp_num = number
            rtn_arr[index] = rtn_arr[move_idx]
            rtn_arr[move_idx] = temp_num
            move_idx += 1

    return rtn_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
