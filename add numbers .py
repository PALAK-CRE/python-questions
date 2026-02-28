class Solution:
    def addTwoNumbers(self, l1, l2):

        n1 = n2 = 0
        p1 = p2 = 1

        # build number correctly
        while l1:
            n1 += l1.val * p1
            p1 *= 10
            l1 = l1.next

        while l2:
            n2 += l2.val * p2
            p2 *= 10
            l2 = l2.next

        total = n1 + n2

        if total == 0:
            return ListNode(0)

        head = tail = None

        while total:
            digit = total % 10
            total //= 10

            node = ListNode(digit)

            if head == None:
                head = tail = node
            else:
                tail.next = node
                tail = node

        return head