# Last updated: 8/14/2026, 2:58:28 PM
1class Solution:
2    def deleteDuplicates(self, head):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        prev = dummy
7        current = head
8
9        while current:
10            duplicate = False
11
12            while current.next and current.val == current.next.val:
13                duplicate = True
14                current = current.next
15
16            if duplicate:
17                prev.next = current.next
18            else:
19                prev = prev.next
20
21            current = current.next
22
23        return dummy.next