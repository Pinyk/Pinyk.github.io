a=int(input("请输入一个100以内的目标值"))
keys=[]
for i in range(50):
     keys.append(i)
values=[]
for j in range(1,51):
     values.append(j)
b=zip(keys,values)
c=dict(b)
print("先遍历字典供参考")
print(c)
for k in range(50):
     for l in range(50):
          if c[k]!=c[l] and c[k]+c[l]==a:
               d=k
               e=l
print(d)
print(e)


     
