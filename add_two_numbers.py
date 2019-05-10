#2 Add Two Numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        head = res
        carry = 0
        while (l1 or l2) or carry:
            summation = 0
            if l1:
                summation += l1.val
                l1 = l1.next
            if l2:
                summation += l2.val
                l2 = l2.next
            if carry:
                summation += carry
            if summation >= 10:
                summation = summation - 10
                carry = 1
            else:
                carry = 0
            print(summation)
            res.val = summation
            if l1 or l2 or carry:
                res.next = ListNode(0)
                res = res.next
        return head
