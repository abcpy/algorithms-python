class Solution:
    def calPoints(self, ops):
        res = []
        for i, char in enumerate(ops):
            if char == 'C':
                res.pop()
            elif char == 'D':
                res.append(2 * int(res[-1]))
            elif char == '+':
                res.append(int(res[-1] + res[-2]))
            else:
                res.append(int(char))
        return sum(res)

if __name__ == '__main__':
    s = Solution()
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(s.calPoints(ops))