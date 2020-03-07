class Solution:
    def add(self, a: int, b: int) -> int:
        while b: 
            a, b = (a ^ b) & 0xFFFFFFFF, ((a & b) << 1) & 0xFFFFFFFF
        return a if a <= 0x7FFFFFFF else ~ a ^ 0xFFFFFFFF
#python无限长整型不会自动溢位