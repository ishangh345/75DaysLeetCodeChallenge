class Solution:
    def subarraySum(self, nums, k):
        count_map = {0: 1}
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            if current_sum - k in count_map:
                count += count_map[current_sum - k]
            
            count_map[current_sum] = count_map.get(current_sum, 0) + 1
        
        return count