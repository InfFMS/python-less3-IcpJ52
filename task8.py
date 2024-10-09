# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить, сколько было введено положительных и
# сколько отрицательных чисел (нули не считать!).
n = int(input())
neg = 0
pos = 0
for _ in range(n):
    num = int(input())
    if num > 0:
        pos += 1
    if num < 0:
        neg += 1
print(f"Положительных чисел: {pos}\nОтрицательных чисел: {neg}")
