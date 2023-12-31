# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.

# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

from random import randint

n = int(input('Введите количество кустов: '))         # Ввод количества кустов
print(bush := [randint(1,4) for _ in range(n)])       # Заполнение списка урожайности рандомом от 1 до 4

max_berries = 0
sum = 0

for i in range(len(bush)+2):                                                      # Проходим количетство раз - длина списка + 2 (собирает ягоды с этого куста и с двух соседних с ним)
    sum = bush[(i-1)%len(bush)] + bush[i%len(bush)] + bush[(i+1)%len(bush)]       # Суммируем кол-во ягод, %len(bush) используем остаток от деления для "бесконечного списка" (из 3-го семинара)
    if max_berries < sum:                                                         # Находим максимальное значение ягод
        max_berries = sum                                                         

print(max_berries)