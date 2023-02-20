import math
import matplotlib.pyplot as plt
import numpy as np

x_old = 0
x_new = 0.1 #x 시작
y_new = 0 #y
steps = 0.1 #스텝 
precision = 0

#그래프 초기 설정 
plt.xlabel('x')
plt.ylabel('y')
plt.grid(color = "gray", alpha=.5)
x = np.arange(0,0.61,0.01) # x 범위

#f(x) 그래프
def f(x):
    C = 0
    return (10 / 4) * x ** 4 - (5 / 3) * x ** 3 + C

plt.plot(x,f(x))

#f'(x) 그래프
def f_prime(x):
    return 10 * x ** 3 - 5 * x ** 2

plt.plot(x,f_prime(x))

plt.legend()

#반복 
while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new = x_old - steps * f_prime(x_old)
    y_new = f(x_new)
    plt.scatter(x_new,y_new)
    print(f"x: {x_new} y: {y_new}, y': {f_prime(x_old)}")
    plt.pause(0.01)

#결과 
print("--------------------")
print(f"Local minimum: x: {x_new} y: {round(y_new,4)}")
print("--------------------")
plt.show()

