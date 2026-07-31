class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)

        required = Counter(words)
        ans = []

        for i in range(len(s) - total_len + 1):

            seen = Counter()

            for j in range(i, i + total_len, word_len):
                word = s[j:j + word_len]
                seen[word] += 1

            if seen == required:
                ans.append(i)

        return ans
        