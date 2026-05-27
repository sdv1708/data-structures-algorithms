class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                parts = []

                while stack and stack[-1] != '[':
                    parts.append(stack.pop())

                stack.pop()  # remove '['

                k = []
                while stack and stack[-1].isdigit():
                    k.append(stack.pop())

                substr = ''.join(reversed(parts))
                repeat = int(''.join(reversed(k)))

                stack.append(repeat * substr)

        return ''.join(stack)