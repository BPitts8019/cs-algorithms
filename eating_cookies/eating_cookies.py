'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache):
    if n < 0:
        return 0
    if n <= 1:
        cache[n] = 1
        return 1

    if cache[n] > 0:
        number_of_ways = cache[n]
    else:
        number_of_ways = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        cache[n] = number_of_ways
    return number_of_ways


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies, [0 for i in range(num_cookies+1)])} ways for Cookie Monster to eat {num_cookies} cookies")
