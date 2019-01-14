#模拟过程
#1 2 3 4 5 6 7 8 9
#1 1 2 3 5 8 13 21 34
def main():
     a=int(input("请输入你想知道的月份\n"))
     b=gao(a)
     print("这个月兔子的总数为%d对"%b)
def gao(n):
     list=[]
     list.append(1)
     list.append(1)
     list.append(1)
     for i in range(3,n+1):
          m=list[i-1]+list[i-2]
          list.append(m)
     return list[n]
main()
