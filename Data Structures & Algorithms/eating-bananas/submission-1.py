import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def opt(p,h):
            left=1
            right=max(p)
            while left<=right:
                mid=(left+right)//2
                total=0
                for i in p:
                    total+=math.ceil(i/mid)
                    if total>h:
                        break
                if total <= h:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        return opt(piles,h)