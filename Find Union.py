class Solution:
    def find_union(self , arr1 , arr2):
        arr1 = set(arr1)
        arr2 = set(arr2)
        ans = arr1.union(arr2)
        return list(ans)
    
solution = Solution()
arr1 =list(map(int,input("Enter the array 1 elements : ").split()))
arr2 =list(map(int,input("Enter the array 2 elements : ").split()))

print(solution.find_union(arr1,arr2))