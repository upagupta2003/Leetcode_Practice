class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor_arr = []

        # print((n//2)+1)

        for i in range(1, (n//2)+1):
            if n%i == 0:
                factor_arr.append(i)
                # print(f"factors : {factor_arr}")
        
        factor_arr.append(n)

        if len(factor_arr) >= k:
            return factor_arr[k-1]

        return -1


        # count = 0
        # for i in range(1,(n//2 + 1)):
        #     if count > k:
        #         break
        #     if n%i == 0:
        #         count += 1
        #     if count == k:
        #         return i
        # if count+1 == k:
        #     return n
        # return -1
