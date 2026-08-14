# Last updated: 8/14/2026, 2:46:43 PM
1class Solution:
2    def addTwoNumbers(self, l1, l2):
3        dummy = ListNode(0)
4        current = dummy
5        carry = 0
6
7        while l1 or l2 or carry:
8            x = l1.val if l1 else 0
9            y = l2.val if l2 else 0
10
11            total = x + y + carry
12
13            carry = total // 10
14            digit = total % 10
15
16            current.next = ListNode(digit)
17            current = current.next
18
19            if l1:
20                l1 = l1.next
21
22            if l2:
23                l2 = l2.next
24
25        return dummy.next