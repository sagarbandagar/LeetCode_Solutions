class Solution:
    def move_zero(self , arr):
        
        #iterate over the array
        for item in arr:
            #check if the item is 0
            if item == 0:
                arr.remove(item)     #remove it
                arr.append(item)     #add it to the end 
        return arr 
    
solution = Solution()
arr = list(map(int,input("Enter the array elements : ").split()))
ans = solution.move_zero(arr=arr)
print(ans)