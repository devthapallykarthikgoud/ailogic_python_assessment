n = int(input())
lst = list(map(int, input().split()))
k = int(input())

m = sum(lst[:k])

maxi = m

for i in range(k,n):
  m = m-lst[i-k]+lst[i]
  maxi = max(maxi,m)
print(maxi)
