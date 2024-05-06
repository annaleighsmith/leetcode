class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in matches.values():
                stack.append(char)
            elif char in matches.keys():
                if not stack or matches[char] != stack.pop():
                    return False
        return not stack


s = "()[]{}"
solution = Solution().isValid(s)
print(solution)
