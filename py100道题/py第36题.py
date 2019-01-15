a=input("请输入首字母（大写）")
if a == 'S':
     b =input("请输入第二个字母（小写）")
     if b == 'a':
         print ('Saturday')
     elif b  == 'u':
         print ('Sunday')
     else:
         print ('error')
elif a == 'F':
     print ('Friday')
elif a == 'M':
     print ('Monday')
elif a == 'T':
     b =input("请输入第二个字母（小写）")
     if b == 'u':
         print ('Tuesday')
     elif b == 'h':
         print ('Thursday')
     else:
         print ('error')
elif a == 'W':
     print ('Wednesday')
else:
     print ('error')
