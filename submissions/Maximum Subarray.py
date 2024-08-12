with open('./temp.txt', 'r') as _:
    hard_one = eval(_.read())

print(type(hard_one))
quit()
def maxSubArray(nums):

    max_so_far = sum(nums)

    subarray_size = len(nums)-1

    while subarray_size > 0:
        for step in range(len(nums)+1-subarray_size):
            max_this_loop = sum(nums[step:step+subarray_size])
            if max_this_loop > max_so_far:
                max_so_far = max_this_loop
        subarray_size -= 1
    return max_so_far


tests = (
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
    (hard_one, None),
)

for input, expected in tests:
    print(f"input: {input}")
    output = maxSubArray(input)
    print(f"expected: {expected}")
    print(f"output: {output}\n")
