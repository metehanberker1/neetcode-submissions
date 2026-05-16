class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        def backtrack(subset, subset_sum, i):
            nonlocal res
            if subset_sum == target:
                res.append(subset[:])
                return
            if i >= len(nums) or subset_sum > target:
                return
            subset.append(nums[i])
            backtrack(subset, subset_sum + nums[i], i)
            subset.pop()
            backtrack(subset, subset_sum, i+1)

        backtrack([], 0, 0)
        return res