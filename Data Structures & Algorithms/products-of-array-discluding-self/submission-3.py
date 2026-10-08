from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max_product: int = 1
        output: list = [0] * len(nums)
        zeros = []

        if all(num == 0 for num in nums):
            return output

        # we still might have partial 0 values in our array..
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
                continue
            max_product *=  nums[i]


        for j in range(len(nums)):
            if any(zero_idx != j for zero_idx in zeros):
                output[j] = 0
                continue

            if nums[j] == 0:
                output[j] = max_product
                continue

            output[j] = int(max_product / nums[j])

        return output

