a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[9,8,7],[6,5,4],[3,2,1]] 
c=[[],[],[]] 
for i in range(3):
   for j in range(3):
       c[i][j] = a[i][j] + b[i][j]
for n in c:
    print(n)
