import os

os.system('cls||clear')

with open('../temp2.txt', 'r') as _:
import os

os.system('cls||clear')

with open('../temp2.txt', 'r') as _:
    hard_one = eval(_.read())



def maxSubArray(nums):

    from itertools import product

    array_len =len(nums)
    array_sum = sum(nums)
    max_so_far = array_sum
    print(array_len)
    
    # progressive left sums
    left_sums  = [0]
    for i in range(array_len-1):
        left_sums.append(left_sums[-1]+nums[i])
    print("left_sums done")
    
    # progressive right sums
    right_sums = [0]
    for i in range(array_len-1):
        right_sums.append(right_sums[-1]+nums[-1-i])
    print("right_sums done")
    
    # all the combinations of left and right sums 
    for left_idx, right_idx in product(range(array_len), repeat=2):
        if left_idx+right_idx<array_len:
        
            # evaluate all subarrays sums by gradually removing elements from the sides
            middle_sum = array_sum - left_sums[left_idx] -right_sums[right_idx]

            # udpating max sum value
            if middle_sum > max_so_far:
                max_so_far = middle_sum
    
    return max_so_far


tests = (
    ([-2, -3, -1], -1),
    ([-2, 1], 1),
    ([-2, -1], -1),
    ([-2, -3, -1], -1),
    ([-2, 1], 1),
    ([-2, -1], -1),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([5, 4, -1, 7, 8], 23),
    ([1], 1),
    ([-1], -1),
    ([1], 1),
    ([-1], -1),
    (hard_one, None),
)

for input, expected in tests:
    if len(input) <= 16:
        print(f"input: {input}")
    else:
        print(f"input: {str(input[:8])[:-1]}, ...]")
    if len(input) <= 16:
        print(f"input: {input}")
    else:
        print(f"input: {str(input[:8])[:-1]}, ...]")
    output = maxSubArray(input)
    print(f"expected: {expected}")
    print(f"output: {output}\n")
