# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".
n = int(input())
min_num = 100
max_num = -100
for _ in range(n):
    num = int(input())
    if (num in range(-99, -9) or num in range(10, 100)) and num % 3 == 0:
        min_num = min(min_num, num)
        max_num = max(max_num, num)
print('нет' if min_num == 100 else f"Минимальное двузначное число, делящееся на 3: {min_num}\nМаксимальное двузначное число, делящееся на 3: {max_num}")
