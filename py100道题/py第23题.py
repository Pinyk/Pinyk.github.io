for i in range(1,1001):
     s=0
     for j in range(1,i):
          if i%j==0:
               s=s+j
     if i==s:
          print(i)
          
