import os


def rob(nums):
    if len(nums) == 1:
        return nums[0]

    def get_next_idx(idx):
        choices = []
        try:
            choices.append((nums[idx+2], idx+2))
        except IndexError:
            pass
        try:
            choices.append((nums[idx+3], idx+3))
        except IndexError:
            pass
        if len(choices) > 0:
            return max(choices, key=lambda x: x[0])[1]
        return None

    def get_idsx(idx):
        idxs = [idx]
        while True:
            next_idx = get_next_idx(idxs[-1])
            if next_idx is not None:
                idxs.append(next_idx)
            else:
                break
        return idxs

    attempt0 = sum([nums[idx] for idx in get_idsx(0)])
    attempt1 = sum([nums[idx] for idx in get_idsx(1)])

    return attempt0 if attempt0 > attempt1 else attempt1


# testing
os.system('cls||clear')

cases = (
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([2, 1, 1, 2], 4),
    ([2, 4, 8, 9, 9, 3], 19),
)

for input, expected in cases:
    print(f"input:    {input}")
    print(f"expected: {expected}")
    print(f"output:   {rob(input)}", end='\n\n')
