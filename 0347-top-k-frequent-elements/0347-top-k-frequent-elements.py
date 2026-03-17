import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        return heapq.nlargest(k, freq.keys(), key=freq.get)