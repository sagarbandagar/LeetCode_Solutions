class Solution:
    def move_zero(self , arr):
        for item in arr:
            if item == 0:
                arr.remove(item)
                arr.append(item)
        return arr 
    
solution = Solution()
arr = list(map(int,input("Enter the array elements : ").split()))
ans = solution.move_zero(arr=arr)
print(ans)