# Last updated: 8/14/2026, 2:52:25 PM
1class Solution:
2    def swapPairs(self, head):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        prev = dummy
7
8        while prev.next and prev.next.next:
9            first = prev.next
10            second = first.next
11
12            # Swap the nodes
13            first.next = second.next
14            second.next = first
15            prev.next = second
16
17            # Move to the next pair
18            prev = first
19
20        return dummy.next