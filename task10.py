# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".
n = int(input())
min_num = 2 * 10 ** 9
max_num = 1
for _ in range(n):
    num = int(input())
    if num != 1:
        is_prime = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = 0
                break
        if is_prime == 1:
            min_num = min(min_num, num)
            max_num = max(max_num, num)
print('нет' if max_num == 1 else f"Минимальное простое число: {min_num}\nМаксимальное простое число: {max_num}")
