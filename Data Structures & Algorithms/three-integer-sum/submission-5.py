class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        head_ptr = 0
        tail_ptr = len(sorted_nums) - 1

        seen: set = set()
        triplets: list[list[int]] = []

        while sorted_nums[head_ptr] <= 0:
            if head_ptr == len(sorted_nums) - 1:
                break
            aux_head = head_ptr + 1
            tail_ptr = len(sorted_nums) - 1

            while aux_head < len(sorted_nums):
                if aux_head >= tail_ptr:
                    break

                if sorted_nums[aux_head] < 0 and sorted_nums[tail_ptr] < 0:
                    break

                if sorted_nums[aux_head] + sorted_nums[tail_ptr] == abs(sorted_nums[head_ptr]):
                    triplet = tuple(sorted([sorted_nums[head_ptr], sorted_nums[aux_head], sorted_nums[tail_ptr]]))
                    if triplet not in seen:
                        seen.add(triplet)
                        triplets.append([sorted_nums[head_ptr], sorted_nums[aux_head], sorted_nums[tail_ptr]])
                    aux_head += 1
                    tail_ptr -= 1
                elif abs(sorted_nums[aux_head] + sorted_nums[tail_ptr]) < abs(sorted_nums[head_ptr]):
                    aux_head += 1
                else:
                    tail_ptr -= 1

            head_ptr += 1

        return triplets
