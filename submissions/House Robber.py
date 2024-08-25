# TODO
# this passes all the tests, but I am surely not proud of it
# it is computationally very expensive
# i should re-do it using data trees

import os


def rob(nums):

    nums_count = len(nums)
    if nums_count == 1:
        return nums[0]

    def rob_from(start):
        """
        given the starting index, 
        returns the largest cumulative addition
        """

        # given the starting index,
        # for each step,
        # get all the possible reachable indexes
        step = 0
        reachable_indexes = []
        # (add whole triangles first)
        triangular = nums_count*(nums_count+1)/2
        while len(reachable_indexes) < triangular:
            reachable_indexes.append([])
            for idx in range(start, start+step+1):
                idx_candidate = 2*step+idx
                if idx_candidate < nums_count:
                    reachable_indexes[-1].append(idx_candidate)
            step += 1
        # (leftovers later)
        while len(reachable_indexes[-1]) > 1:
            reachable_indexes.append(reachable_indexes[-1][2:])

        # for each step,
        # get all the possible reachable values
        steps = [[nums[idx] for idx in step] for step in reachable_indexes]

        # then, for each step,
        # all the highest cumulative values
        cum_steps = [steps[0]]
        for curr_vals in steps[1:]:
            if curr_vals:
                prev_cums = [
                    max(prev_cum_vals)
                    for prev_cum_vals
                    in zip(cum_steps[-1][:-1], cum_steps[-1][1:])
                ]
                curr_cums = [
                    prev_cum + curr_val
                    for prev_cum, curr_val
                    in zip(prev_cums[:len(curr_vals)], curr_vals[1:])
                ]
                cum_steps.append([])
                cum_steps[-1].append(curr_vals[0]+cum_steps[-2][0])
                for curr_cum in curr_cums:
                    cum_steps[-1].append(curr_cum)
                if len(cum_steps[-1]) < len(curr_vals):
                    cum_steps[-1].append(curr_vals[-1] + cum_steps[-2][-1])

        # return the maximum value
        return max(max(sublist) for sublist in cum_steps)

    # the max we can rob will be obtained
    # by either starting from house 0 or from house 1
    return max([rob_from(0), rob_from(1)])


# testing
os.system('cls||clear')

cases = (
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([2, 1, 1, 2], 4),
    ([2, 4, 8, 9, 9, 3], 19),
    ([0], 0),
    ([4, 1, 2, 7, 5, 3, 1], 14),
    ([0, 0], 0),
    ([1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3], 42),
    ([1, 2, 3, 5, 8, 13, 21, 34], None),
    ([
        226, 174, 214, 16, 218, 48, 153, 131, 128, 17, 157, 142, 88, 43, 37,
        157, 43, 221, 191, 68, 206, 23, 225, 82, 54, 118, 111, 46, 80, 49, 245,
        63, 25, 194, 72, 80, 143, 55, 209, 18, 55, 122, 65, 66, 177, 101, 63,
        201, 172, 130, 103, 225, 142, 46, 86, 185, 62, 138, 212, 192, 125, 77,
        223, 188, 99, 228, 90, 25, 193, 211, 84, 239, 119, 234, 85, 83, 123,
        120, 131, 203, 219, 10, 82, 35, 120, 180, 249, 106, 37, 169, 225, 54,
        103, 55, 166, 124
    ],
        7102),
)

for index, (input, expected) in enumerate(cases):
    if index != 0:
        print(f"---")
    print(f"input:    {input}")
    print(f"expected: {expected}")
    print(f"output:   {rob(input)}")
