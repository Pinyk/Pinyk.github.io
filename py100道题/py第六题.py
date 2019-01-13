list=[1,1,2]
m=3
for i in range(10):
    m=list[i+1]+list[i+2]
    list.append(m)
    m=m+1
print(list)
    
