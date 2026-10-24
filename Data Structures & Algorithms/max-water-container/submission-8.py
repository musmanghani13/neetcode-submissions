class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left: int = 0
        right: int = len(heights) - 1
        volumn: int = 0

        while right > left:
            width: int = abs(left - right)
            height: int = min(heights[left], heights[right])

            if (width * height) > volumn:
                volumn = width * height

            if heights[left] > heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:
                left += 1
                right -= 1

        return volumn
