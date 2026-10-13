class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Step 1: Square all elements and sort them in ascending order
        squares = sorted([x * x for x in nums])
        
        n = len(squares)
        mid = n // 2
        
        # Step 2: Subtract the smaller half and add the larger half
        return sum(squares[mid:]) - sum(squares[:mid])