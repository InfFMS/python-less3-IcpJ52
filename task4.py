# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить сумму тех введённых чисел, которые делятся на 5.
sm = 0
while True:
    n = int(input())
    if n == 0:
        print(f"Сумма чисел, делящихся на 5: {sm}")
        break
    if n % 5 == 0:
        sm += n
