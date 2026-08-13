class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=set()
        nums=sorted(nums)
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                if nums[left]+nums[right]+nums[i]==0:
                    res.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                
                elif nums[left]+nums[right]+nums[i]>0:
                    right-=1
                else:
                    left+=1
        answer = [list(x) for x in res]
        return answer
