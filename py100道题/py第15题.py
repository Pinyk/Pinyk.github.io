for i in range(100,1000):
     a=(i//100)**3
     b=(i%100//10)**3
     c=(i%10)**3
     if a+b+c==i :
          print(i)
