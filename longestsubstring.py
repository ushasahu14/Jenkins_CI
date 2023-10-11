class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        lst=[]
        d=dict()
        if not s:
            return 0
        while l<=len(s)-1:

            for char in s[l:]:
            
                if char not in d:
                    d[char]=1
                else:
                    break
            lst.append([''.join(d.keys()),len(d)])
            d.clear()
            l+=1

        lst.sort(key=lambda x:x[1],reverse=True)
        return lst[0][1]