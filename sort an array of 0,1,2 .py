
class Solution:
    def sortColors(self, nums) -> None: 
        n = len(nums)
        c0,c1,c2 =0,0,0

        #run a loop over the array to get the count of 0 , 1 amd 2
        for i in range(n):
            if nums[i] ==0:
                c0+=1
            if nums[i]==1:
                c1+=1
            if nums[i]==2:
                c2+=1

            if nums[i] is not 0 or 1 or 2:
                return f'array should contain only 0 , 1 or 2'

        #start the array elements from 0 to the count of c0
        for i in range(0,c0):
            nums[i] =0

        #start the array elements from c0 to the count of c0+c1
        for i in range(c0,c0+c1):
            nums[i] =1

        #start the array elements from c0+c1 to the count of c0+c1+c2
        for i in range(c0+c1,c0+c1+c2):
            nums[i] = 2

        return nums
    
solution =  Solution()
List = list(map(int,input("Enter array elements of 0,1,2 : ").split()))
print(solution.sortColors(List))

        