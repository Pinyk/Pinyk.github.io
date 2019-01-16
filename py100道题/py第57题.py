a=int(input('输入一个数:'))
def gao(i,j):
    if i==j or j==1:
        return 1
    else:
        return gao(i-1,j-1)+gao(i-1,j)
def main():
     for i in range(1,a+1):
         for j in range(1,i+1):
             print(gao(i,j),end="")
         print()
main()
