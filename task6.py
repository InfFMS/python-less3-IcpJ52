# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
n = int(input())
if n == 0:
    print('Нет чисел для анализа.')
else:
    max_el = n
    min_el = n
    while True:
        n = int(input())
        if n == 0:
            print(f"Минимальное число: {min_el}\nМаксимальное число: {max_el}")
            break
        max_el = max(max_el, n)
        min_el = min(min_el, n)
