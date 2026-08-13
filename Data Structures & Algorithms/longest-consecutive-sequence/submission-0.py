class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num=set(nums)
        longest=0
        for i in nums:
            if i-1 not in set_num:
                length=0
                while i in set_num:
                    length+=1
                    i+=1
                longest=max(longest,length)

        return longest