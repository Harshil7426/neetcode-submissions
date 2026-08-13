class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        
        for j in t:
            if j not in freq or freq[j]==0:
                return False
            freq[j]-=1
        return True
