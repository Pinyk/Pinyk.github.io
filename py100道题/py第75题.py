a=input("请输入一个字符串")
b=list(a)
c=len(b)
if b[0]!=b[1]:
     print("0")
else:
     for i in range(1,c):
          if b[i]!=b[i+1] and b[i-1]!=b[i]:
               print(i)
               break
          else:
               print("-1")
#程序有bug
