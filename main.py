# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите кол-во элементов первого множества "))
m = int(input("Введите кол-во элементов второго множества "))
massive_n = []
massive_m = []
print(f"введите {n} элементов для первого множества")
for i in range(0,n):
    v = int(input())
    massive_n.append(v)
print(f"введите {m} элементов для второго множества")
for i in range(0,m):
    v = int(input())
    massive_m.append(v)

massive = massive_n + massive_m
massive.sort()
massive = set(massive)
print(massive)