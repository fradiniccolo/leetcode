class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # test rows
        for row in board:
            row_nums = [i for i in row if i != "."]
            if len(set(row_nums)) != len(row_nums):
                return False

        # test columns
        for col in zip(*board):
            col_nums = [i for i in col if i != "."]
            if len(set(col_nums)) != len(col_nums):
                return False

        # test boxes
        for offset_x in [0, 3, 6]:
            for offset_y in [0, 3, 6]:

                # text box
                box = []
                for x in range(3):
                    for y in range(3):
                        box.append(board[x+offset_x][y+offset_y])
                box_nums = [num for row in box for num in row]
                box_nums = [i for i in box_nums if i != "."]
                if len(set(box_nums)) != len(box_nums):
                    return False

        return True
