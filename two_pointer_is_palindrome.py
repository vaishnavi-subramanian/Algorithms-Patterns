class Solution:
    def is_palindrome_iterative(s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    print(is_palindrome_iterative("level"))  # Output: True
    print(is_palindrome_iterative("python")) # Output: False