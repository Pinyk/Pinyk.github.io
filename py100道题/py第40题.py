n=int(input("输入一个正整数"))
m=0
for i in range(2,n):
     for j in range(2,i):
          if i%j==0:
               break
     else:
          m=m+1
print(m)
