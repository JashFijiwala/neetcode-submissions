class Solution:
    def create_key(self, word):
        freq = [0] * 26

        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        return tuple(freq
        )
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            key = self.create_key(word)

            if key not in result:
                result[key] = []

            result[key].append(word)

        return list(result.values())
        