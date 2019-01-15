def main():
     a=gao(5)
     print(a)
def gao(b):
     if b==1:
          return 1
     else:
          return b*gao(b-1)
main()
     
