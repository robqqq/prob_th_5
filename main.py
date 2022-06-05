import math
import numpy as np
import matplotlib.pyplot as plt

x = [0.83, -0.48, -1.35, 0.31, 0.59, 1.35, -0.30, -0.24, 0.51, 0.26,
     0.73, 0.00, 1.59, 0.17, -0.45, 1.60, -0.18, -1.73, 0.03, 1.70]
x.sort()
print("Вариационный ряд:", x)

x_min = x[0]
x_max = x[-1]
print("Xmin =", x_min)
print("Xmax =", x_max)

r = x_max - x_min
print("R =", r)

n = int(1 + math.log2(len(x)))
h = r / n
x_int = {}
print("Интервальный ряд:")
for i in np.arange(x_min, x_max + h/2, h):
    count = 0
    for j in x:
        if i - h/2 <= j < i + h/2:
            count += 1
    x_int[i] = count
    print(i - h/2, "-", i + h/2, ":", count)

mx = 0
for i in list(x_int):
    mx += i * x_int[i]
mx /= len(x)
print("Mx =", mx)

deviation = 0
for i in list(x_int):
    deviation += ((i ** 2) * x_int[i])
deviation /= len(x)
deviation -= mx ** 2
deviation = deviation ** (1/2)
print("Среднеквадратичное отклонение -", deviation)

f = {x_min: 0}
print("Эмпирическая функция распределения:")
for i in list(x_int):
    print("F*(", i - h/2, ") =", f[i])
    f[i + h] = f[i] + x_int[i] / len(x)
print("F*(", x_max + h/2, ") =", list(f.values())[-1])

plt.figure()
plt.title("Эмпирическая функция распределения")
for i in list(f):
    plt.plot([i, i + h], [f[i], f[i]])
# plt.plot(list(f), list(f.values()))
plt.grid(True)
plt.show()

p = {}
for i in list(x_int):
    p[i] = x_int[i] / len(x)

plt.figure()
plt.title("Гистограмма приведённых частот")
plt.bar(list(p), list(p.values()))
plt.grid(True)
plt.show()

plt.figure()
plt.title("Полигон приведённых частот")
plt.plot(list(p), list(p.values()))
plt.scatter(list(p), list(p.values()))
plt.grid(True)
plt.show()