class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ca = 0
        ha = ca
        for i in gain:
            ca = ca + i
            ha = max(ca,ha)
        return ha


