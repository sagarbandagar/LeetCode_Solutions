class Solution:
    def MajorityElement(self , arr):
        # len of the array
        n = len(arr)

        #import counter 
        from collections import Counter 

        counter = Counter(arr)

        #run a loop over the counter items to check the frequency 
        for key , value in counter.items():

            # check if value > n//2 times , if yes return the value
            if value > (n//2):
                return key
            
        return f'No element is greater than n//2'
            
solution =Solution()
arr=list(map(int,input("Enter the array :  ").split()))
ans = solution.MajorityElement(arr)
print(ans)