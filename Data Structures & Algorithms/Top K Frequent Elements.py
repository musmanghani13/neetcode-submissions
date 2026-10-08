class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = Counter(nums)
        k_repeating: list = []

        for number, frequency in counter.items():
            heapq.heappush(heap, (-frequency, number)) # max heap based on frequency

        for counter in range(k):
            k_repeating.append(heap[0][1])
            heapq.heappop(heap)

        return k_repeating
