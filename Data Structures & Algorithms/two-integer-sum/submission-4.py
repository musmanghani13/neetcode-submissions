class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers: dict[int, int] = {}

        for index, num in enumerate(nums):
            numbers[num] = index

        for x_index, num in enumerate(nums):
            x = num
            determined_y = target - x
            if determined_y in numbers and numbers[determined_y] != x_index:
                return [x_index, numbers[determined_y]]
