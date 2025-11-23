from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None ):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        环形链表
        :param head: 一个链表的头结点
        :return: 链表中是否有环
        时间复杂度：O(N)
        空间复杂度：O(N)
        """
        # 思路：哈希集合
        # 1.用哈希表来存储所有已经访问过的节点。
        # 2.每次我们到达一个节点，如果该节点已经存在于哈希表中，则说明该链表是环形链表，否则就将该节点加入哈希表中。
        seen = set()
        while head is not None:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

    def pointCycle(self, head: Optional[ListNode]) -> bool:
        """
        时间复杂度：O(N)
        空间复杂度：O(1)
        """
        # 思路：快慢指针,如果两指针同时指向一个结点，说明链表有环
        slow = head
        fast = head.next
        while fast:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False

# 测试代码
if __name__ == "__main__":
    solution = Solution()

    # 测试1：有环的链表
    print("=== 测试有环链表 ===")
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # 形成环：4 -> 2

    result1 = solution.pointCycle(node1)
    print(f"有环链表检测结果: {result1}")  # 应该输出: True

    # 测试2：无环的链表
    print("\n=== 测试无环链表 ===")
    node5 = ListNode(1)
    node6 = ListNode(2)
    node7 = ListNode(3)

    node5.next = node6
    node6.next = node7
    # node7.next = None (默认，无环)

    result2 = solution.hasCycle(node5)
    print(f"无环链表检测结果: {result2}")  # 应该输出: False

    # 测试3：空链表
    print("\n=== 测试空链表 ===")
    result3 = solution.hasCycle(None)
    print(f"空链表检测结果: {result3}")  # 应该输出: False

    # 测试4：单个节点自成环
    print("\n=== 测试单个节点环 ===")
    node8 = ListNode(1)
    node8.next = node8  # 指向自己形成环

    result4 = solution.hasCycle(node8)
    print(f"单个节点环检测结果: {result4}")  # 应该输出: True
