a = []
sum = 0.0
for i in range(3):
     a.append([])
     for j in range(3):
          a[i].append(float(input("依次输入矩阵各点:\n")))
for i in range(3):
     sum += a[i][i]
print(sum)
