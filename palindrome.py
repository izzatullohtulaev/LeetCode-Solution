class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            temp = str(x)
            temp = temp[::-1]
            if str(x) == temp:
                return True
            else:
                return False
