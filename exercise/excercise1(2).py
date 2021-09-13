class Solution(object):
	def twoSum(self, nums, target):
		dic = {}
		for i in range(len(nums)):
			if nums[i] in dic:
				return [dic[nums[i]], i]
			else:
				dic[target - nums[i]] = i

a = Solution()
print(a.twoSum([1,2,3,4], 7))