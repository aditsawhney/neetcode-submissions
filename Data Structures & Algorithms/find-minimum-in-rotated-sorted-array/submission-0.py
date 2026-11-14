class Solution:
    def findMin(self, nums: List[int]) -> int:
        # one half must be sorted. if it's left, nums[left] would be smallest, then we would search in right for a smaller element. else if right is sorted, nums[mid] would be sorted, and we would search in left for a smaller element

        left, right = 0, len(nums)-1
        res = nums[left]

        while left <= right:
            mid = (left+right)//2

            # if left is sorted
            if nums[left] <= nums[mid]:
                res = min(res, nums[left])
                left = mid+1    # check in right for smaller element
            else:   # if right is sorted
                res = min(res, nums[mid])
                right = mid-1   # check in left for smaller element
            
        
        return res