# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.
prime = 0
composite = 0
while True:
    n = int(input())
    if n == 0:
        print(f"Простых чисел: {prime}")
        print(f"Составных чисел: {composite}")
        break
    if n > 0:
        if n == 1:
            continue
        is_prime = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                composite += 1
                is_prime = 0
                break
        if is_prime == 1:
            prime += 1
