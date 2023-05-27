class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                nums[i] < target and (i+1 == len(nums) or nums[i+1] > target)
                return i+1
n1=Solution()
num=[1,4,5,7,9]
print(n1.searchInsert(num,))
class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] < target and (i+1 == len(nums) or nums[i+1] > target):
                    return i+1
