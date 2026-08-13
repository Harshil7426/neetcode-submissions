class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev=stack.pop()
                warmer[prev]=i-prev
            stack.append(i)
        return warmer