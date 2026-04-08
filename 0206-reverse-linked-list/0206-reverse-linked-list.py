class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # store next
            curr.next = prev     # reverse link
            prev = curr          # move prev
            curr = nxt           # move curr

        return prev