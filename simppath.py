class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Stack will store [character, count]

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1  # Increment count if same char
            else:
                stack.append([c, 1])  # New char with count 1

            if stack[-1][1] == k:
                stack.pop()  # Remove group of k identical chars

        # Rebuild the final string from the stack
        res = ""
        for char, count in stack:
            res += char * count
        return res
