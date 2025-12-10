from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, nxt: Optional['ListNode'] = None):
        self.val = val
        self.next = nxt

    # 辅助：把 Python list 转成链表
    def from_list(arr: list[int]) -> Optional["ListNode"]:
        dummy = cur = ListNode()
        for v in arr:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """返回该链表的中间结点，或偏右的中间结点（偶数时）、快慢指针"""
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        """翻转链表、双指针"""
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        """
        回文链表
        :param head: 一个链表的头结点
        :return:判断是否为回文链表
        时间复杂度： O(n)，其中 n 是链表的长度（节点个数）。
        空间复杂度： O(1)。
        """
        # 思路：双指针
        # 1.先找到中心结点，再进行中心结点右侧的链表反转
        # 2.左指针在原head，右指针在反转链表的头结点，即原链表的最后一个结点
        # 3.两指针同时进行移动，遇到不同值则返回false，否则true
        left = head
        middle = self.middleNode(head)
        right = self.reverseList(middle)
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

if __name__ =="__main__":
    sol = Solution()
    head1 = ListNode.from_list([1, 2, 2, 1])
    head2 = ListNode.from_list([1, 2])
    print(sol.isPalindrome(head1)) # true
    print(sol.isPalindrome(head2))  # false