import os


def rob(nums):

    nums_count = len(nums)
    if nums_count == 1:
        return nums[0]

    def rob_from(start):
        """
        given the stating index, 
        returns, for each step, the largest cumulative addition
        """

        # let's get a list, for each step,
        # of all the possible reachable indexes
        step = 0
        idxs = []
        contained = True
        while contained:
            idxs.append([])
            for idx in range(start, start+step+1):
                idx_candidate = 2*step+idx
                if idx_candidate < nums_count:
                    idxs[-1].append(idx_candidate)
                else:
                    contained = False
            step += 1

        # then, for each step,
        # all the possible reachable values
        steps = [[nums[idx] for idx in step] for step in idxs]
        print(steps)
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

                # we can save memory by removing old steps
                #cum_steps.pop(0)
        print(cum_steps)
        # the maximum value, given a certain starting index,
        # will be on the last cumulative step
        return max(max(sublist) for sublist in cum_steps[-2:])

    # the absolute max we can rob is reachable either starting from 0 or from 1
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
    ([0,0], 0),
    ([1,1,3,6,7,10,7,1,8,5,9,1,4,4,3], 42),
    ([1, 2, 3, 5, 8, 13, 21, 34], None),
    # ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233], None),
)

for index, (input, expected) in enumerate(cases):
    if index != 0:
        print(f"\n---\n")
    print(f"input:    {input}")
    print(f"expected: {expected}")
    print(f"output:   {rob(input)}")
