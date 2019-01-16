print("请输入5个数")
list1=[]
for i in range(5):
     list1.append(int(input("")))
print(list1)
list2=[0,1,2,3,4]
a=zip(list2,list1)
b=dict(a)
c=max(list1)
d=min(list1)
for i in range(0,5):
     if b[i]==c:
          e=i
for i in range(0,5):
     if b[i]==d:
          f=i
t=list1[0]
list1[0]=list1[e]
list1[e]=t
n=list1[4]
list1[4]=list1[f]
list1[f]=t
print(list1)

