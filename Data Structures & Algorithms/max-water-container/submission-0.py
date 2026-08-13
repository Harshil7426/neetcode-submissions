class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=0
        right=n-1
        maxarea=0
        while left<right:
            less=min(heights[left],heights[right])
            area=less*abs(left-right)
            maxarea=max(area,maxarea)
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        return maxarea
        
