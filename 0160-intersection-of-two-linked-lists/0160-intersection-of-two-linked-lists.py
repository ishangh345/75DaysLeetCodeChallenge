class Solution:
    def getIntersectionNode(self, headA, headB):

        a = headA
        b = headB

        while a != b:

            if a:
                a = a.next
            else:
                a = headB

            if b:
                b = b.next
            else:
                b = headA

        return a