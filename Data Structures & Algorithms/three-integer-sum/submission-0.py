class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use a loop to iterate through the entire array, and select the 
        # first element. for the next 2 elements, use the same approach
        # as two sum ii. first, arrange the elements in ascending order

        nums.sort()
        result = []

        for i in range(len(nums)-2):

            # skip duplicate values for 1st element
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                    # skip duplicate values for 2nd and 3rd elements
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        
        return result
                    