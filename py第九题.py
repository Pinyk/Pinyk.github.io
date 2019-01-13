def main():
     a=int(input("请输入楼梯的阶数\n"))
     b=gao(a)
     print("有%d种方法"%b)
def gao(n):
     list=[]
     list.append(0)
     list.append(1)
     list.append(2)
     for i in range(3,n+1):
          m=list[i-1]+list[i-2]
          list.append(m)
     return list[n]
main()

