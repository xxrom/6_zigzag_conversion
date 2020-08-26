class Solution:
  def convert(self, s: str, n: int) -> str:
    ans = ''
    allLevels = []

    for i in range(n):
      allLevels.append([])

    # print(allLevels)
    size = len(s)
    i = 0
    inc = +1
    level = 0
    count = 0

    while i < size:
      char = s[i]
      print('char %s [%d]' % (char, i))

      allLevels[level] += char
      # print(allLevels)

      i += 1
      level += inc

      if (level == n - 1):
        inc *= -1

      if (level == 0):
        inc *= -1


    # print(allLevels)
    for i in range(n):
      ans += ''.join(allLevels[i])

    return ans

my = Solution()

s = "PAYPALISHIRING"
n = 3
trueAns= "PAHNAPLSIIGYIR"

ans = my.convert(s, n)
print("ans", ans, ans == trueAns)

# Runtime: 64 ms, faster than 72.25% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 14 MB, less than 20.94% of Python3 online submissions for ZigZag Conversion.