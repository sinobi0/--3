
"""
1. Дан список. Получите новый список, в котором каждое значение будет удвоено:
[1, 2, 3] --> [2, 4, 6]
"""
lst = [int(i) for i in input('Введите список чисел').split()]  # Ввод списка с числами
for i in range(len(lst)):                                      # Цикл по индексам
    lst[i]+=lst[i]                                             # На каждом индексе изменяем число, прибавляя к нему это же  число
print(lst)
"""
2. Дан список. Возведите в квадрат каждый из его элементов и получите сумму всех полученных квадратов:
[1, 2, 3] --> 14 --> 1^2 + 2^2 + 3^2 = 14
"""
lst = [1,2,3]  # Список чисел
c=0            # Счетчик   
for i in lst:  # Цикл по значениям
    c+=i*i     # Записываем в c  каждое число из списка в квадрате и прибавляем
print(c)
"""
3. Дана строка 'Hello world'. Проверьте, если в этой строке есть символ пробела - " ", тогда преобразуйте строку к верхнему регистру, если же нет, тогда к нижнему.
**
s = 'Hello world'
if stm:
    pass
else:
    pass
"""
s = 'Hello world'
if ' ' in s:    # Если пробел есть в списке, 
    s=s.upper() # тогда преобразуем в верхний регистр
    print(s)    # Вывод числа
else:
    s = s.lower()
    print(s)
"""
4. Выведите все года, начиная с 1900 по 2020
**
1900 год
1901 год
1902 год
n год
2020 год
"""
for i in range(1900,2021):
    print(i, 'год')
