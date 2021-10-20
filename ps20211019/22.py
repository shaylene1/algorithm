class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(0, 0, "", res, n)
        return res

    def dfs(self, countleft, countright, path, res, n):
        if countleft < countright or countleft > n or countright > n:
            return

        if countleft == countright == n:
            res.append(path)

        for i in "()":
            if i == "(":
                self.dfs(countleft + 1, countright, path + i, res, n)
            if i == ")":
                self.dfs(countleft, countright + 1, path + i, res, n)
