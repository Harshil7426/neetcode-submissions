# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        for i in range(k-1):
            head=head.next
        while temp is not None:
            start = temp
            count=0
            while temp is not None and count<k:
                slowtemp = temp
                temp=temp.next
                count+=1
            if count !=k:
                break
            prev=temp
            curr=start
            while curr !=temp:
                nxt=curr.next
                curr.next=prev
                prev = curr
                curr=nxt 
            count = 0
            temp2 = start
            while temp2.next!=None and count<k:
                count+=1
                temp2=temp2.next
            if count==k:
                start.next = temp2                
        return head
