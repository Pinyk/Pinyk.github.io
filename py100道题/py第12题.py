import math
a=int(input("请输入一个整数"))
b=2**31-1
c=math.log(b)//math.log(3)
d=math.pow(3,c)
if d%a==0:
     print("这个数是三的幂次方")
else:
     print("这个数不是三的幂次方")

