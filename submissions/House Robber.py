import os

def rob(nums):

    attempt0 = 0
    attempt1 = 0
    
    for idx, num in enumerate(nums):
        pass
        


# testing

os.system('cls||clear')

cases = (
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([2,1,1,2], 4)
)

for input, expected in cases:
    print(f"input:    {input}")
    print(f"expected: {expected}")
    print(f"output:   {rob(input)}")
