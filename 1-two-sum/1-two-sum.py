class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            t2 = target - nums[i]
            n2 = nums[i+1:]
            for j in range(len(n2)):
                if n2[j] == t2:
                    k = i + j + 1
                    return [i,k]