class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
                continue

            if char in (')', '}', ']'):

                if stack:
                    if pairs[char] != stack.pop():
                        return False
                else:
                    return False

        if stack:
            return False

        return True

        