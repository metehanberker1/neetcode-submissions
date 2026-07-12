class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        volume = 0

        while i < j:
            volume = max(volume, (j-i) * min(heights[i], heights[j]))
            if heights[i] >= heights[j]:
                j -= 1
            else:
                i += 1

        return volume