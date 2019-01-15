a=int(input())
b=1
c=a%10
print("%d"%c,end='')
while a//10!=0:
     a=a//10
     c=a%10
     print('%d'%c,end='')
     b=b+1
print()
print(b)
     
