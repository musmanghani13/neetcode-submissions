class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers: dict[int, list] = {}
        for index, num in enumerate(nums):
            # if num > target:
            #     continue
            if num in numbers:
                numbers[num].append(index)
            else:
                numbers[num] = [index]

        for num_key, index_values in numbers.items():
            x = num_key
            determined_y = target - x

            if determined_y == x and len(numbers[x]) > 1:
                return  [index_values[0], index_values[1]]
            elif determined_y in numbers and determined_y != x:
                indexes_y = numbers[determined_y]
                return [index_values[0], indexes_y[0]]

