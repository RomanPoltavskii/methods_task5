import math

def f(x):
    return 1 / (x**2 * math.log(x) ** 2)

def trap(f, a, b, h):
    s = 0.5 * (f(a) + f(b))
    x = a + h
    while (x <= b - h):
        s += f(x)
        x += h
    return h * s

I_exact = 0.326396 # точное значение
res = (trap(f, 2, 8, 0.001)) # значение по формуле трапеций
Delta_I_abs = abs(I_exact - res)
Delta_I_rel = Delta_I_abs / abs(I_exact)

# выводим результаты
print("Приближенное значение интеграла: ", res)
print("Абсолютная погрешность: ", Delta_I_abs)
print("Относительная погрешность: ", Delta_I_rel)
