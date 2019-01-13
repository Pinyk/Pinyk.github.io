import math
print("10000以内可以找到3个这样的数，分别是")
for i in range(10000):
    a=math.sqrt(i+100)
    c=math.sqrt(i+100+168)
    if int(a)==a and int(c)==c:
        print(i)
