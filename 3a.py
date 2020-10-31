'''
count ways function
main function
'''


import functools
from functools import lru_cache

letters_allowed, max_adj, length = (int(x) for x in input().split())
n = int(input())

@lru_cache(maxsize = None)
def count_ways(prefix = '', adj_count = 0, prev_letter = -1):

    ways = 0
    if adj_count > max_adj:
        return 0
    if len(prefix) == length:
        return 1

    for letter in range(letters_allowed):

        letter = str(letter)
        if letter == prev_letter:
            ways += count_ways(prefix + letter, adj_count + 1, letter)
        else:
            ways += count_ways(prefix + letter, 1, letter)

    return ways


def get_ans(n):

    ans = ''
    i = 0
    prev = '-1'
    adj_count = 1

    while len(ans) != length:
        
        for pref in range(letters_allowed):
            if str(pref) == prev:
                new_adj = adj_count + 1
                new_perms = count_ways(ans + str(pref), adj_count = new_adj, prev_letter = ans + str(pref))

            else:
                new_adj = adj_count + 0
                new_perms = count_ways(ans + str(pref), adj_count = new_adj, prev_letter = ans + str(pref))

            if new_perms + i > n:
                break

            else:
                i += new_perms

        ans += str(pref)
        adj_count = new_adj

    return ans

answer = get_ans(n)
print(''.join(chr(65 + int(x)) for x in answer))

        
