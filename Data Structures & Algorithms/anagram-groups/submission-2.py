class Solution:
    def create_freq(self, word):
        freq = [0] * 26
        for letter in word:
            freq[ord(letter) - ord('a')] += 1

        return tuple(freq)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}
        final = []

        for s in strs:
            freq = self.create_freq(s)
            if freq not in result:
                result[freq] = []
            result[freq].append(s)

        for key, value in result.items():
            final.append(value)

        return final
            

        