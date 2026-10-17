class Solution:
    def fib(self, n: int) -> int:
        #base case
        if  n == 0:
            return 0
        if n == 1:
            return 1
        #recursive case
        return self.fib(n-1) + self.fib(n-2)

'''
#iterative approach
 class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        prev2, prev1 = 0, 1
        for _ in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1
'''



'''
class solution:
    def fib(self, n :int)-> int :
        if n <= 1:
            return n
        
        df=[0] * (n+1)
        dp[1] = 1
        for _ in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
'''