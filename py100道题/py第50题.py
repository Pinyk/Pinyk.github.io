#移动后的位置用0补位
list=[1,2,3,4]
a=int(input("请输入一个非负数"))
for i in range(a):
     list.append(0)
j=3
while j>0:
     list[j+3+a]=list[j+3]
     list[j+3]=0
     j=j-1
print(list)

