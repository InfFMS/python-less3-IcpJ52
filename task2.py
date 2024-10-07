# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.
two_digit = 0
other = 0
while True:
    n = float(input())
    if n == 0:
        print(f"Двузначных чисел: {two_digit}")
        print(f"Других чисел: {other}")
        break
    if n in range(10, 100):
        two_digit += 1
    else:
        other += 1
