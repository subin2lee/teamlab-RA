from itertools import combinations
def soultion(nums):
    char = 0
    memo = []
    for c in combinations(nums,3):
        plus_c = sum(c)
        for x in range(2,plus_c):
            if (plus_c) % x != 0:
                pass
            else:
                memo.append(1)
        if len(memo) == 0:
            char += 1
        memo = []
    return char
nums = [1,2,3,4]
print(soultion(nums))