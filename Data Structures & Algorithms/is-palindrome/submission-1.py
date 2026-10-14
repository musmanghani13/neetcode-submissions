class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()

        head_ptr = 0
        tail_ptr = len(s) - 1

        while tail_ptr > head_ptr:
            if s[head_ptr] != s[tail_ptr]:
                break
            head_ptr += 1
            tail_ptr -= 1
        else:
            return True

        return False
