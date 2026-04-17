import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = { ch:0 for ch in string.ascii_lowercase}
        n1 = len(list(s))
        n2 = len(list(t))
        if n1 != n2:
            return False
        for i in range(n1):
            dictionary[s[i]] += 1
            dictionary[t[i]] -= 1
        return all(v==0 for v in dictionary.values())