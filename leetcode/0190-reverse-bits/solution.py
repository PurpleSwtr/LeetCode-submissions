class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = n.zfill(32)
        b = []
        for num in range(0, len(n)):
            b.append(n[num])
        s = int(''.join(b[::-1]), 2)
        return s
