class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ letter.lower() for letter in s if letter.isalnum()]
        print(s)
        i,j = 0, len(s) -1

        while i<=j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else: return False
        return True  