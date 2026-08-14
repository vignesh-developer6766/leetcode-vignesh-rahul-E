# Last updated: 8/14/2026, 3:02:12 PM
1class Solution:
2    def sortList(self, head):
3        if not head or not head.next:
4            return head
5
6        # Find the middle
7        slow = head
8        fast = head.next
9
10        while fast and fast.next:
11            slow = slow.next
12            fast = fast.next.next
13
14        # Split the list
15        mid = slow.next
16        slow.next = None
17
18        # Sort both halves
19        left = self.sortList(head)
20        right = self.sortList(mid)
21
22        # Merge
23        return self.merge(left, right)
24
25    def merge(self, left, right):
26        dummy = ListNode(0)
27        current = dummy
28
29        while left and right:
30            if left.val <= right.val:
31                current.next = left
32                left = left.next
33            else:
34                current.next = right
35                right = right.next
36
37            current = current.next
38
39        if left:
40            current.next = left
41
42        if right:
43            current.next = right
44
45        return dummy.next