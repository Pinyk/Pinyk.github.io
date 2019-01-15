def main():
    list=[]
    for m in range(10):
        list.append(int(input()))
    maopao(list)
    print(list)
def maopao(list):
    t=0
    for i in range(0,9):
        for j in range(0,9-i):
            if list[j]>list[j+1]:
                t=list[j+1]
                list[j+1]=list[j]
                list[j]=t
main()
