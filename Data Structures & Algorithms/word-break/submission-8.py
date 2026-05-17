class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def dfs(remainder):
            if remainder in memo:
                return memo[remainder]
            if not remainder:
                return True

            for word in wordSet:
                if remainder.startswith(word) and dfs(remainder[len(word):]):
                    memo[remainder] = True
                    return memo[remainder]

            memo[remainder] = False
            return memo[remainder]

        return dfs(s)