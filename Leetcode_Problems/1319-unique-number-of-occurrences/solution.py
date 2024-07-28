class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # res = {}
        # count = 0
        # for i in range(len(arr)):
        #     if i==0 or arr[i] not in res.keys():
        #         count = arr.count(i)
        #         res[arr[i]] = count
        #         print()
        # return True if len(res.values()) == len(set(res.values())) else False

        # res = [] ## store the coumt
        # for i in set(arr):
        #     curr_ct = arr.count(i)
        #     if curr_ct in res:
        #         return False
        #     res.append(curr_ct)
        # return True

        from collections import Counter
        count = Counter(arr)

        return True if len(count.values()) == len(set(count.values())) else False



