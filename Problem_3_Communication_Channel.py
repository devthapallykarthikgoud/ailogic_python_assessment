s = input()

max_len = 0

for i in range(len(s)):
  t = ""

  for j in range(i, len(s)):
      if s[j] not in t:
          t += s[j]
          max_len = max(max_len, len(t))
      else:
          break

print(max_len)
