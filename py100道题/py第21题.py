a = input('请输入字符串：')
b=0
c=0
d=0
e=0
for i in a:
    if i.isalpha():
        b +=1
    elif i.isnumeric():
        c +=1
    elif i.isspace():
        d +=1
    else:
        e +=1
print('字母=%d'%b)
print('数字=%d'%c)
print('空格=%d'%d)
print('其他=%d'%e)
