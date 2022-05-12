# https://leetcode.com/problems/majority-element/

def majority_element(nums):
    counts, unique_nums = ([], [])

    for num in nums:
        if num in unique_nums:
            counts[unique_nums.index(num)] += 1
        else:
            unique_nums.append(num)
            counts.append(1)
    
    most_freq_index = counts.index(max(counts))
    most_freq = unique_nums[most_freq_index]

    return most_freq if counts[most_freq_index] > len(nums)/2 else None

print(majority_element([3, 2, 3]))
print(majority_element([2,2,1,1,1,2,2]))

# ---- Accepted LeetCode Solution ----

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts, unique_nums = ([], [])

        for num in nums:
            if num in unique_nums:
                counts[unique_nums.index(num)] += 1
            else:
                unique_nums.append(num)
                counts.append(1)
        
        most_freq_index = counts.index(max(counts))
        most_freq = unique_nums[most_freq_index]
    
        return most_freq if counts[most_freq_index] > len(nums)/2 else None
