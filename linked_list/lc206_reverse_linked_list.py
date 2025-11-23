from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    # 辅助：把 Python list 转成链表
    @staticmethod
    def from_list(arr: list[int]) -> Optional["ListNode"]:
        dummy = cur = ListNode()
        for v in arr:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    # 辅助：把链表转回 Python list，方便打印/断言
    def to_list(self) -> list[int]:
        out, cur = [], self
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out

class Solution:
    def reverselink(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        反转链表
        :param head: 一个链表的头结点
        :return: 链表反转后的链表的头节点
        时间复杂度 O(N) ： 遍历链表使用线性大小时间。
        空间复杂度 O(1) ： 变量 pre 和 cur 使用常数大小额外空间。
        """
        # 思路：迭代法（双指针）头插法
        pre = None
        cur = head
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def reverselink2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        时间复杂度 O(N) ： 遍历链表使用线性大小时间。
        空间复杂度 O(N) ： 遍历链表的递归深度达到 N ，系统使用 O(N) 大小额外空间。
        """
        # 思路：递归法
        # 首先「递」到链表末尾，把末尾节点作为新链表的头节点 rev_head
        # 然后在「归」的过程中，把经过的节点依次插在新链表的末尾（尾插法）
        if head is None or head.next is None:
            return head
        rev_head = self.reverselink2(head.next) # 「递」到链表末尾，拿到新链表的头节点
        tail = head.next # 在「归」的过程中，head.next 就是新链表的末尾
        tail.next = head # 把 head 插在新链表的末尾
        head.next = None # 如果不写这行，新链表的末尾两个节点成环，这俩节点互相指向对方
        return rev_head


# 本地自测
if __name__ == "__main__":
    sol = Solution()
    head = ListNode.from_list([1, 2, 3, 4, 5])
    new_head = sol.reverselink2(head)
    print("反转结果:", new_head.to_list())          # 期望 [5, 4, 3, 2, 1]