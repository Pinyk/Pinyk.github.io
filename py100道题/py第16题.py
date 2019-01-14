while 1:
    n = int(input('请输入一个整数：'))
    print('%d='%n,end='')
    while n>1:
        for i in range(2,n+1):
            if n%i==0:
                n=n/i
                if n==1:
                    print('%d'%i,end='')
                else:
                    print('%d*'%i,end='')
                break
    break
