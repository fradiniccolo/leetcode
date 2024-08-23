import os


def maxSubArray(nums):
    
    candidates = [range(nums[0], nums[0])]
    max_values = [nums[0]]

    for num in nums[1:]:

        candidate = candidates[-1]

        if candidate.stop + num > candidate.start:
            candidates[-1] = range(candidate.start, candidate.stop+num)
            
            if candidates[-1].stop > max_values[-1]:
                max_values[-1] = candidates[-1].stop
        else:
            candidates.append(range(num, num))
            max_values.append(num)

        
    print(candidates)
    print(max_values)
    
    return max(max_values)

# testing
os.system('cls||clear')


# with open('../temp2.txt', 'r') as _:
#    hard_one = eval(_.read())

tests = (
    ([-2, -3, -1], -1),
    ([-2, 1], 1),
    ([-2, -1], -1),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([5, 4, -1, 7, 8], 23),
    ([1], 1),
    ([-1], -1),
    # (hard_one, None),
)

for input, expected in tests:
    if len(input) <= 16:
        print(f"input: {input}")
    else:
        print(f"input: {str(input[:8])[:-1]}, ...]")
    output = maxSubArray(input)
    print(f"expected: {expected}")
    print(f"output: {output}\n")
