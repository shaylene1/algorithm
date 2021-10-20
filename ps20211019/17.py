class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ""
        dic = {"2": "abc",
               "3": "def",
               "4": "ghi",
               "5": "jkl",
               "6": "mno",
               "7": "pqrs",
               "8": "tuv",
               "9": "wxyz"}
        res = []
        self.dfs(digits, "", res, dic)
        return res

    def dfs(self, digits, path, res, dic):
        if not digits:
            res.append(path)
            return

        for i in dic[digits[0]]:
            self.dfs(digits[1:], path + i, res, dic)
