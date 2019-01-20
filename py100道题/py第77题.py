sum=0
for i in range(0,8):
     for j in range(0,8):
          if (i+j)%2!=0:
               sum=sum+1
          else:
               pass
print("一共可以组成%d个奇数"%sum)
