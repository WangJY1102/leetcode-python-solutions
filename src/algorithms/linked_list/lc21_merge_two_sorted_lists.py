from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, nxt: Optional['ListNode'] = None):
        self.val = val
        self.next = nxt

class Solution:
    def MergeTwoLists(self, l1: ListNode, l2: ListNode) ->ListNode:
        """递归，两个递增链表合并成一个递增链表
            先比较两个来个链表的头结点
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.MergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.MergeTwoLists(l1, l2.next)
            return l2


# ===== 本地调试 =====
def build_list(nums):
    """工具：把 Python 列表转成链表，返回头节点"""
    dummy = ListNode()
    curr = dummy
    for v in nums:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_list(head):
    """工具：把链表打印成 Python 列表"""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

if __name__ == "__main__":
    # 手动输入
    nums1 = list(map(int, input("链表1（空格分隔）: ").split()))
    nums2 = list(map(int, input("链表2（空格分隔）: ").split()))

    l1 = build_list(nums1)
    l2 = build_list(nums2)

    merged = Solution().MergeTwoLists(l1, l2)
    print("合并后链表：", end="")
    print_list(merged)