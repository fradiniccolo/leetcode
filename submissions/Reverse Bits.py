class Solution:
    def reverseBits(self, n: int) -> int:
        
        bin_n = str(bin(n))[2:][::-1]
        
        while len(bin_n) < 32:
            bin_n += '0'

        return int(bin_n, 2)
