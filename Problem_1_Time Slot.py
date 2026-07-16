n= int(input())
t=[]
for i in range(n):
  start, end = map(int, input().split())
  t.append([start,end])
t.sort()
result=[]
for i in t:
  if result == []:
    result.append(i)
  else:
    last = result[-1]
    if i[0] <= last[1]:
      last[1] = max(last[1],i[1])
    else:
      result.append(i)
for i in result:
  print(f"{i[0]} {i[1]}")
