n,y,r=eval(input("依次输入年,月,日"))
dic={1:'0',2:'31',3:'59',4:'90',5:'120',6:'151',7:'181',8:'212',9:'243',10:'273',11:'304',12:'334'}
sum=int(dic[y])+r
flag=0
if n%400==0 or (n%4==0 and n%100!=0):
    flag=1
if flag==1 and y>2:
    sum=sum+1
print("这是这一年中的第%d天"%sum)
    
