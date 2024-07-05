class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = Next
    

class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        p = head
        while p.next is not None:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
    
if __name__ == "__main__":
    s = Solution()
    print(s.deleteDuplicates([1, 1, 2]))