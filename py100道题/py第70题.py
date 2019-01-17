def main():
     a=int(input("请输入一个数"))
     if a%2==0:
          gao(a)
     else:
          yu(a)
def gao(n):
     i=2
     sum=0
     while i<=n:
          j=1/i
          sum=sum+j
          i=i+2
     print(sum)
def yu(n):
     i=1
     sum=0
     while i<=n:
          j=1/i
          sum=sum+j
          i=i+2
     print(sum)
main()     
          
