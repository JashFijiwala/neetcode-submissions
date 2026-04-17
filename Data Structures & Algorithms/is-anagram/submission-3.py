import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {a:0 for a in string.ascii_lowercase}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            check[s[i]] += 1
            check[t[i]] -= 1
        
        return all(v == 0 for v in check.values())

        
        