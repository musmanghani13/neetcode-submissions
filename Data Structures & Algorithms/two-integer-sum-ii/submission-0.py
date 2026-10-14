class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1

        while tail > head:
            current_sum = numbers[head] + numbers[tail]
            if current_sum == target:
                return [head + 1, tail + 1]
            elif current_sum > target:
                tail -= 1
            elif current_sum < target:
                head += 1
