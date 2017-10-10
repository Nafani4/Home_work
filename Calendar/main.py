from spisok_zadach import spisok_zadach
from dobavit_zadachu import dobavit_zadachu
from otredaktirovat_zadachu import otredaktirovat_zadachu
from zavershit_zadachu import zavershit_zadachu
from nachat_zadachu_zanovo import nachat_zadachu_zanovo

print("""\nЕжедневник. Выберите действие\n
    1. Вывести список задач
    2. Добавить задачу
    3. Отредактировать задачу
    4. Завершить задачу
    5. Начать задачу сначала
    6. Выход
    """)
n = int(input('Введите число '))

while n < 6:
    if n == 1:
        print(spisok_zadach(), '\n')
        n = int(input('Введите число '))

    if n == 2:
        print(dobavit_zadachu(), '\n')
        n = int(input('Введите число '))
    

    if n == 3:
        print(otredaktirovat_zadachu(), '\n')
        n = int(input('Введите число '))


    if n == 4:
        print(zavershit_zadachu(), '\n')
        n = int(input('Введите число '))

    if n == 5:
        print(nachat_zadachu_zanovo(), '\n')
        n = int(input('Введите число '))

else:
    print('\nПока')
