class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        # binary search tree
        low, high = 0, len(A) - 1
        
        while low < high:
            
            mid = int((low + high) / 2)
            
            if A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid
        
        return low
