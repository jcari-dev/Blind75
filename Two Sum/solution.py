class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if nums[i] in pair:
                return [i, pair[nums[i]]]

            if compliment not in pair:
                pair[compliment] = i
            