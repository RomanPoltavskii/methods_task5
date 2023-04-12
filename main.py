import math
from scipy.optimize import minimize_scalar
def f(x):
    return 1 / (x**2 * math.log(x) ** 2)

def ddf(x): # вторая производная
    return (2*(3*math.log(x)**2 + 5* math.log(x) + 3))/x**4 * math.log(x) ** 4
def trapezoidal_rule(f, a, b, n):
    # метод трапеций
    h = (b - a) / n
    sum = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i * h
        sum += f(x)
    return h * sum


a, b = 2, 8
n = 100
res = (trapezoidal_rule(f, a, b, n)) # значение по формуле трапеций


def accuracy(ddf, a, b, n):
    max_ddf = minimize_scalar(lambda x: -abs(ddf(x)), bounds=(a, b), method='bounded')
    h = (b - a) / n
    return -(((b - a)*h**2)/12)*round(abs(max_ddf.fun), 5)

print("Приближенное значение интеграла: ", res)
print(str(accuracy(ddf, a, b, n)))