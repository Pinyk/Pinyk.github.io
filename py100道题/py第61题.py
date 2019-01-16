a,b,c=eval(input("请输入3个数 以（，），格式输入"))
if a>b:
     t=b
     b=a
     a=t
if a>c:
     t=c
     c=a
     a=t
if b>c:
     t=c
     c=b
     b=t
print(a,b,c)
     
