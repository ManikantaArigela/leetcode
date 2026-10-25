class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for i in s:
            freq[i]+=1
        print(freq)
        sorted_dict = sorted(freq.items(),key = lambda x : x[1], reverse = True)
        print(sorted_dict)
        result = ""
        for c,f in sorted_dict:
            print(c,f)
            result += c*f
        return result