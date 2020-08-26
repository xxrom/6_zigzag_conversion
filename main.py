class Solution:
  def convert(self, s: str, n: int) -> str:
    allLevels = [''] * n

    inc = +1 if n > 1 else 0
    level = 0

    for char in s:
      allLevels[level]  += char

      level += inc

      if level == n - 1 or level == 0:
        inc *= -1

    return ''.join(allLevels)

my = Solution()

s = "PAYPALISHIRING"
n = 3
trueAns= "PAHNAPLSIIGYIR"

ans = my.convert(s, n)
print("ans", ans, ans == trueAns)

# Runtime: 36 ms, faster than 99.99% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 13.8 MB, less than 79.72% of Python3 online submissions for ZigZag Conversion.