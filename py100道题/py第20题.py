a=int(input("输入一个右界"))
for i in range(1,a+1):
     if i%3==0 and i%5!=0:
          print("Fizz")
     if i%3!=0 and i%5==0:
          print("Buzz")
     if i%3==0 and i%5==0:
          print("FizzBuzz")
     if i%3!=0 and i%5!=0:
          print(i)
