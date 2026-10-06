class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_bra =0
        min_adds =0
        for i in s :
            if i == "(" :
                open_bra += 1
            else:
                if open_bra > 0 :
                    open_bra -= 1
                else:
                    min_adds +=1
        return min_adds + open_bra