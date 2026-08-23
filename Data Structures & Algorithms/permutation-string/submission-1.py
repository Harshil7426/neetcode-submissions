class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq={}
        for i in s1:
            freq[i]=freq.get(i,0)+1
        current={}
        for i in range(len(s1)):
            current[s2[i]]=current.get(s2[i],0)+1
        left=0
        right=len(s1)-1
        while right<len(s2):
            if freq==current:
                return True
            right += 1
            if right < len(s2):
                current[s2[right]] = current.get(s2[right], 0) + 1
            current[s2[left]]-=1
            if current[s2[left]]==0:
                del current[s2[left]]
            left+=1
        return False
        

            
        

        