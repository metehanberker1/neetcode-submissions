class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dictionary:
                return [dictionary[complement], i]
            dictionary[num] = i