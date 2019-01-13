print("请输入任意三个数:")
x,y,z=eval(input(",,,格式输入"))
if x>y:
    t=y
    y=x
    x=t
if x>z:
    t=z
    z=x
    x=t
if y>z:
    t=z
    z=y
    y=t
print(x,y,z)
