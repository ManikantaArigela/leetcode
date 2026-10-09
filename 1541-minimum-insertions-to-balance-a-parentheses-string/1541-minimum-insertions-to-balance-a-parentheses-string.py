class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_brackets = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                open_brackets += 1
                i += 1
            else:
                # We encountered a right parenthesis ')'
                # Check if it has a consecutive partner ')'
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    # Missing one ')'
                    insertions += 1
                    i += 1
                
                # Now match these two right parentheses with an available open bracket
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    # No open bracket available, need to insert one '('
                    insertions += 1
                    
        # Any remaining unmatched open brackets need two ')' each
        insertions += open_brackets * 2
        return insertions