# f(x) = sin(x)^2 - cos(x)^2
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

from sympy import Symbol, solve, diff, evalf, solveset, S, pprint, sin, cos
from sympy.plotting import plot

x = Symbol('x')
function = sin(x)**2 - cos(x)**2

# Определить корни
print(f'Нули функции\n')
pprint(solveset(function, x, domain=S.Reals), use_unicode=True)


# Определить промежутки, на котором f > 0
print(f'Промежутки, на котором f > 0\n')
pprint(solveset(function > 0, x, domain=S.Reals), use_unicode=True)
# Определить промежутки, на котором f < 0
print(f'Промежутки, на котором f < 0\n')
pprint(solveset(function < 0, x, domain=S.Reals), use_unicode=True)

# Вычислить вершину 
function_diff = diff(function, x)
print(f'Производная\n')
print(function_diff)

# Экстремумы
pprint(solveset(function_diff, x, domain=S.Reals), use_unicode=True)

# Найти интервалы, на которых функция возрастает (решить неравенства где производная больше или меньше нуля)
# Найти интервалы, на которых функция убывает

pprint(solveset(function_diff > 0, x, domain=S.Reals), use_unicode=True)
pprint(solveset(function_diff < 0, x, domain=S.Reals), use_unicode=True)

# Построить график
print(f'График функции\n')
plot(function).show()