a=0
for i in range(101,201):
     for j in range(2,i):
          if i % j == 0:
               break
     else:
          print(i)
          a=a+1
print("有%d个素数"%a)
               
