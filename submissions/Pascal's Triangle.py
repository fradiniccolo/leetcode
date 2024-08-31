class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        p = [[1]]
        if numRows == 1:
            return p

        if numRows >= 2:
            while len(p) < numRows:
                latest_row = p[-1]
                new_row = [1, 1]
                for i, j in zip(latest_row[:-1], latest_row[1:]):
                    new_row.insert(-1, i+j)
                p.append(new_row)
            return p
