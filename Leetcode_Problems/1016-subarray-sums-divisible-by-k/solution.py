class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        total = 0
        count = collections.defaultdict(int)
        count[0] = 1
        for num in nums:
            total += num
            mod = total % k
            ans += count[mod]
            count[mod] += 1
        return ans
