class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        uniq=set()
        maxi=0
        while right<len(s):
            if s[right] in uniq:
                while s[right] in uniq:
                    uniq.discard(s[left])
                    left+=1
            uniq.add(s[right])
            maxi=max(maxi,len(uniq))
            right+=1
        return maxi
            
