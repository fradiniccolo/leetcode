class Solution:
    def rob(self, nums: List[int]) -> int:

        class Node:

            def __init__(self, value=None, nodes_in=None, nodes_out=None) -> None:
                self.value = value
                self.nodes_in = nodes_in if nodes_in is not None else []
                self.nodes_out = nodes_out if nodes_out is not None else []
                self.max_cum_value = None

            def add_node_in(self, node_in):
                self.nodes_in.append(node_in)

            def add_node_out(self, node_out):
                self.nodes_out.append(node_out)

            def eval_max_cum_value(self):
                if self.max_cum_value is None:
                    if self.nodes_in:
                        cum_values = [
                            node.eval_max_cum_value()+self.value
                            for node in self.nodes_in
                        ]
                        self.max_cum_value = max(cum_values)
                    else:
                        self.max_cum_value = self.value
                return self.max_cum_value

        nums_count = len(nums)

        nodes = [Node(num) for num in nums]

        for index, node in enumerate(nodes):
            if index > 1:
                node.add_node_in(nodes[index-2])
            if index > 2:
                node.add_node_in(nodes[index-3])
            if index < nums_count-2:
                node.add_node_out(nodes[index+2])
            if index < nums_count-3:
                node.add_node_out(nodes[index+3])

        for node in nodes:
            node.eval_max_cum_value()

        return max(nodes, key=lambda node: node.max_cum_value).max_cum_value
