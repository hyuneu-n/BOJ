import sys
input=sys.stdin.readline

n=int(input())
lst=[]

for _ in range(n):
  weight,height=map(int, input().split())
  lst.append((weight,height))

for i in lst:
    rank = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")