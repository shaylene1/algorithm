class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # sliding window
        maxi = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxi = max(maxi, count)
            else:
                count = 0
        return maxi

