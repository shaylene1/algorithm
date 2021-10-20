class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            i = abs(i)
            if nums[i - 1] >= 0:
                nums[i - 1] = -nums[i - 1]
            else:
                res.append(i)
        return res
