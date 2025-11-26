from typing import Optional

class ListNode:
    def __init__(self, value: int = 0, nxt: Optional['ListNode'] = None):
        self.val = value
        self.next = nxt

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        相交链表：判断两个链表是否相交
        :param headA: 一个链表的头节点
        :param headB: 另一个链表的头节点
        :return:相交则返回两个单链表相交的起始节点，否则返回返回 null
        时间复杂度：O(m+n)，其中 m 和 n 是分别是链表 headA 和 headB 的长度。需要遍历两个链表各一次。
        空间复杂度：O(m)，其中 m 是链表 headA 的长度。需要使用哈希集合存储链表 headA 中的全部节点。
        """
        # 思路：哈希集合
        # 首先遍历链表 headA，并将链表 headA 中的每个节点加入哈希集合中。
        # 然后遍历链表 headB，对于遍历到的每个节点，判断该节点是否在哈希集合中。
        visited = set()
        temp = headA
        while temp:
            visited.add(temp)
            temp = temp.next

        temp = headB
        while temp:
            if temp in visited:
                return temp
            temp = temp.next

        return None

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        相交链表：判断两个链表是否相交
        :param headA: 一个链表的头节点
        :param headB: 另一个链表的头节点
        :return:相交则返回两个单链表相交的起始节点，否则返回返回 null
        时间复杂度：O(m+n)，其中 m 和 n 是分别是链表 headA 和 headB 的长度。两个指针同时遍历两个链表，每个指针遍历两个链表各一次.
        空间复杂度：O(1).
        """
        # 思路：双指针
        # 指针 A 先遍历完链表 headA ，再开始遍历链表 headB，共走a+(b−c)
        # 指针 B 先遍历完链表 headB ，再开始遍历链表 headA，共走b+(a−c)
        # 此时指针 A , B 重合，并有两种情况：同时指向「第一个公共节点」/同时指向null
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

# ===== 本地构造器 =====
def build_list(nums: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in nums:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def build_intersect(a: list[int], b: list[int], intersect_from: int) -> tuple[ListNode, ListNode, Optional[ListNode]]:
    """
    a 独立段 + 公共段
    b 独立段
    intersect_from: 公共段起始下标（相对于 a）
    """
    common = build_list(a[intersect_from:])   # 公共段
    headA = build_list(a[:intersect_from])
    tailA = headA
    while tailA.next:
        tailA = tailA.next
    tailA.next = common                       # a 连到公共段

    headB = build_list(b)                     # b 独立段
    tailB = headB
    while tailB.next:
        tailB = tailB.next
    tailB.next = common                       # b 也连到同一批公共段
    return headA, headB, common

# ===== 自测 =====
if __name__ == "__main__":
    # 例：a = [4,1,8,4,5]  b = [5,0,1,8,4,5]  相交于 8（下标 2 of a）
    headA, headB, expect = build_intersect(
        a=[4, 1, 8, 4, 5],
        b=[5, 0, 1],
        intersect_from=2
    )

    sol = Solution()
    intersect_node = sol.getIntersectionNode(headA, headB)

    if intersect_node:
        print("相交节点值：", intersect_node.val)  # 8
        print("与期望节点同一对象？", intersect_node is expect)  # True
    else:
        print("无相交")