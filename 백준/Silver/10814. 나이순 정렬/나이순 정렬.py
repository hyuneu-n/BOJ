n=int(input())
lst=[]
for _ in range(n):
  age,name=input().split()
  lst.append([int(age),name])
  
lst.sort(key=lambda x:int(x[0]))
for i in lst:
    print(i[0],i[1])