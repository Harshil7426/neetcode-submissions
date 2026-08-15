class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def divide_num(n,d):
            if n%d==0:
                return n//d
            return (n//d)+1
                


        def opt(p,h):
            left=1
            right=max(p)
            while left<=right:
                mid=(left+right)//2
                total=0
                for i in p:
                    total+=divide_num(i,mid)
                    if total>h:
                        break
                if total <= h:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        return opt(piles,h)