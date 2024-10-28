class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        ans =[None] * n

        posIndex ,negIndex = 0, 1
        for i in range(n):
            if (nums[i] > 0):
                ans[posIndex] = nums[i]
                posIndex+=2
            else:
                ans[negIndex] = nums[i]
                negIndex+=2

        return ans

solution =  Solution()
print(solution.rearrangeArray(nums=list(map(int,input("Enter the array : ").split()))))
        