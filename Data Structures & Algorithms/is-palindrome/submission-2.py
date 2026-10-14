class Solution:
    def isPalindrome(self, s: str) -> bool:
        head_ptr = 0
        tail_ptr = len(s) - 1

        while tail_ptr > head_ptr:
            if s[head_ptr].isalnum() and s[tail_ptr].isalnum():
                if s[head_ptr].lower() != s[tail_ptr].lower():
                    return False
                head_ptr = head_ptr + 1
                tail_ptr = tail_ptr - 1
            elif not s[head_ptr].isalnum():
                head_ptr = head_ptr + 1
            elif not s[tail_ptr].isalnum():
                tail_ptr = tail_ptr - 1
        return True
