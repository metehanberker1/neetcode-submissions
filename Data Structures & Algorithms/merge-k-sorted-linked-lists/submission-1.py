# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        for i, l in enumerate(lists):
            pointer = l
            j = 0

            while pointer:
                heapq.heappush(nodes, (pointer.val, i, j, pointer))
                pointer = pointer.next
                j += 1

        res = ListNode()
        dummy = ListNode()
        dummy = res

        while nodes:
            res.next = heapq.heappop(nodes)[3]
            res = res.next

        return dummy.next