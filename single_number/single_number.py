'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    data = {}
    for number in arr:
        if number in data:
            data[number] += 1
        else:
            data[number] = 1

    for (key, value) in data.items():
        if value < 2:
            return key

    return None


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 3, 4, 4, 5, 5, 1, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
