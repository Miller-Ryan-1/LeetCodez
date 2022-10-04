class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = []
        for i in nums:
            if i in unique:
                unique.remove(i)
            else:
                unique.append(i)
        return unique[0]
            