import sys  
class Solution:
    def MaxSum(self , arr , n ):
        sum =0
        maxi = -sys.maxsize-1

        # run loop over the array 
        for i in range(n):   
            
            # add the array element    
            # Until the sum is greater than zero keep on adding the next element  
            sum+=arr[i]          

            #check if the sum is greater than maxi , then assign sum to maxi
            if(sum > maxi):      
                maxi = sum 
            
            # check is sum is less than zero , if yes then make sum as zero (0)
            if (sum < 0):       
                sum =0

        return maxi 
    
solution = Solution()
arr = list(map(int,input("Enter the array : ").split()))
ans = solution.MaxSum(arr , len(arr))
print(f'Maximum subarray sum is : ',ans)