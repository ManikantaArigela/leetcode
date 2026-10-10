from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_ops = k1 + k2
        
        if sum(diffs) <= total_ops:
            return 0
            
        count = Counter(diffs)
        # Sort unique differences in descending order
        unique_diffs = sorted(count.keys(), reverse=True)
        
        # We iterate through the unique differences from largest to smallest
        for i in range(len(unique_diffs)):
            d = unique_diffs[i]
            if d == 0:
                break
                
            freq = count[d]
            # Next smaller difference level available (or 0 if it's the last one)
            next_d = unique_diffs[i + 1] if i + 1 < len(unique_diffs) else 0
            
            # How many steps can we reduce this current level `d` down to `next_d`?
            diff_height = d - next_d
            ops_needed = freq * diff_height
            
            if total_ops >= ops_needed:
                total_ops -= ops_needed
                count[d] = 0
                count[next_d] += freq
            else:
                # We can only partially reduce this level
                full_steps = total_ops // freq
                remainder = total_ops % freq
                
                count[d] -= freq
                count[d - full_steps] += freq - remainder
                count[d - full_steps - 1] += remainder
                total_ops = 0
                break
                
        # If there are still leftover operations after everything has been flattened to 0
        if total_ops > 0:
            return 0

        ans = 0
        for d, freq in count.items():
            ans += freq * (d ** 2)
            
        return ans