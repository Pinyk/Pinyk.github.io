import string
def gao(c,a):
     if a==0:
       return 0
     else:
          print (c[a-1])
          return gao(c,a-1)
def main():
     b = input('输入一个字符串:')
     c=list(b)
     a = len(c)
     gao(c,a)
main()
