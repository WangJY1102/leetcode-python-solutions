class Solution:
    def Valid(self, s: str) -> bool:
        """用哈希表和栈，匹配括号是否有效"""
        # 符号总数为单数，肯定不正确
        if len(s) % 2 != 0:
            return False
        # 哈希表存储正确的符号对
        dict = {")": "(", "}": "{", "]": "["}
        stack = list()
        for ch in s:
            # 如果符号为右括号，则判断相应的左括号是不是在栈的最后一位，或栈是否为空
            if ch in dict:
                if stack[-1] != dict[ch] or not stack:
                    return False
                stack.pop()
            else:
                # 如果符号为左括号，直接入栈
                stack.append(ch)
        return not stack

if __name__ == "__main__":
    s = input("只能输入()[]{}其中的符号：")
    reduce = Solution().Valid(s)
    print(reduce)