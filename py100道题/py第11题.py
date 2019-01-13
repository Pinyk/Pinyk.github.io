def main():
     a=int(input("请输入一个整数"))
     gao(a)
def gao(a):
     list=[]
     while a!=0:
          list.append(a%2)
          a=a//2
     b=len(list)
     c=0
     for i in range(0,b):
          if list[i]==1:
               c=c+1
     print(list)
     print(c)
main()
          
          
     
