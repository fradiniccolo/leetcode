class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        size = len(matrix)

        # mapping matrix elements coordinates before and after the rotation
        # through a dictionary
        coord_start = [(i, j) for i in range(size) for j in range(size)]
        coord_end = [(j, (size - 1) - i) for i, j in coord_start]
        rotation_map = dict(zip(coord_start, coord_end))


        # build a list of rotation paths while empting the dictionary
        def pick_element():
            return list(rotation_map.keys())[0]

        rotation_paths = [[pick_element()]]
        while rotation_map:
            try:
                latest_element = rotation_paths[-1][-1]
                rotation_paths[-1].append(rotation_map[latest_element])
                rotation_map.pop(latest_element)
            except:
                rotation_paths.append([pick_element()])

        # apply the mapped rotations to the original matrix
        # by cycling through the paths, one couple of values per time
        for rotation_path in rotation_paths:
            for index, couple in enumerate(zip(rotation_path[:-1], rotation_path[1:])):
                coord0, coord1 = couple
                row0, col0 = coord0
                row1, col1 = coord1

                # 1. the 2nd value is stored for the next cycle
                value_to_store = matrix[row1][col1]

                # 2. the value from the previous cycle
                #    (or the 1st value if the path begun)
                #    overrides the 2nd value
                if index == 0:
                    value_to_write = matrix[row0][col0]
                matrix[row1][col1] = value_to_write

                # preparing for the next cycle
                value_to_write = value_to_store

        return matrix
