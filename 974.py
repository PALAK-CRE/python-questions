class Solution:
    def subarraysDivByK(self, nums, k):
        count = 0
        prefix_sum = 0
        
        remainder_count = {0: 1}  # base case

        for num in nums:
            prefix_sum += num
            
            remainder = prefix_sum % k
            # handle negative remainder
            if remainder < 0:
                remainder += k
            
            if remainder in remainder_count:
                count += remainder_count[remainder]
            
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        
        return count