class Solution:
    def twoSum(self, nums: 'list[int]', target:'int') -> 'list[int]':
        for i in range(len(nums)):
            for k in range(len(nums)):
                if nums[i] + nums[k] == target:
                    if i == k:
                        return False
                    else:
                        return [i, k]

s = Solution()
print(s.twoSum([1,2,3,4], 7))
