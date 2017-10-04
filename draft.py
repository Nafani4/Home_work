#def f(lst):
#    lst.append(x)
#f(1,4,5,6)
#print(lst)

#def f()

#lst = [14, 8, 3, 1, 89, 2, 45]
#print(len(lst))
#print(lst)
#for i<
#print(lst[1])
#for i in range(0, len(lst)):
 #   sum = int(lst[i])
#    print(i, 'значение', sum)

#s = 'Я,,,,,,бы изменил мир, но бог не дает исходники'
#s = list(s)
#s.remove(',')
#s.reverse()
#print(s)

#l = [3,2,3,4]
#print(l)
#l.reverse()
#print(l)

#string = 'Я бы изменил мир, но бог не дает исходники'
#string = ''.join(string.split())
#print(string)
#a.reverse()

#s = 'Я бы изменил мир, но бог не дает исходники'
#l = s.split()
#s1 = ''
#for i in l:
#    s1 += i + ''
#print(s1)

#lst1 = 'кри'
#lst2 = 'при'
#if lst1[0] == lst2[0]:
#    print('ura', '\n')
#else:
#    print('ne ura')
#if lst1[2] == lst2[2]:
#    print('ura', '\n')
#else:
#    print('ne ura')
#def is_palindrome(s)
#s = 'соуд лк дуос'
s = 'Сел в оЗере березов лес'
print(s)
s.lower()
#s = 'я бы изменил мир, но бог не дает исходникя'
print('Оригинал со строчными:', s)
l1 = s.split()
print('Оригинал в список:', l1)
l2 = ''.join(l1)
print('Список в строку без пробелов:', l2)
s2 = list(l2)
print('Строка без пробелов в список', s2)
#Создаём клон списка без пробелов
s3 = s2[:]
print('Копия списка без пробелов', s3)
s3.reverse()
print('Реверс списка без пробелов', s3)
print(s3)
print(s2)
m = len(s2)
#if s2[0] == s3 [0]:
#    print('Ravno')
#else:
#    print ('Ne ravno')
for i in range(m):
    if s2[i] == s3[i]:
        print(s2[i], s3[i])
        if i == m-1:
            print(True)
    else:
        print(False)
        break
i = i + 1

#for i in range(m): 
#    if s2[i] != s3[i]:
#        print('Ne ravno', '\n')
#        break
#    i = i + 1
#else:
 #       print('Ravno')
    
#else:
#      print('ne ura')

#s2 = ''.join(l1)
#print(s2, l1)
#l = s.split()
#s1 = ''.join(l)
#print(s1)
#s2 = list(s1)
#s3 = s2[:]
#s2.reverse()
#s21 = ''.join(s2)
#s31 = ''.join(s3)
#print(s31[0], s21[0])
#print(s2, '\n\n', s3, s21, s31)
#if s2[0] == s3[0]:
#    print(s2[0])
#    print('ura')
#else:
#    print('ne ura') 
#t=set(s21)^set(s31)
#print(t)
#s = 'я бы изменил мир, но бог не дает исходники'
#s1 = list(s)
#s3 = ''.join(s1)
#s1.reverse()
#s1.remove(' ')
#print(s1)
#print(s3)



#a = [1, 2, 3]
#for x in a:
#    print(a[x-1], end='')

#t=list('ав пxcv')
#p=t.strip('')
#print(t)
#print(a)
#b = a.reverse()
#print(a.reverse())

#i=0
#for i in range(0,len(l)):
#    if l[i]=
#    znach = l[i]
#    print(znach)
#sum = 
#def a(chars=None):

#print(s.strip)
#print(s)
#for i in lst:
#    sum += x
#    print(sum(lst))
#print(sum(lst))
#    i = i + 1
#print(i)
#print(c)
#def a(arg=None):
#    return a.strip(arg) 
#stroka=a 
#def bubble_sort(lst):
#    result = lst                    #Результатом выполнение функции является список
#a=[1,1,8,4,6,2]
#print(a)
#    m = len(lst) - 1                #Определяем количество проходов по списку, как количество элементов списка -1.
                                    #-1 чтобы не превысить индекс списка после сравнения предпоследнего
                                    #элемента с последним
#    while m>0:                      #Начинаем цикл, который будет продолжаться для всех m > 0, начиная с
                                    # m равным (блина списка - 1)
#        for i in range(m):          #Выполнение цикла для каждого индекса i, начиная со значения 0,
                                    #т.е. с 1го элемента списка, до конца текущего списка
                                    #Количество проходов будет уменьшаться, т.к. каждый проход "выталкивает
                                    #максимальное значение на последнее место рассматриваемую позицию
                                    #Количество проходов будет каждый раз уменьшаться на 1 (m=m-1)
#            if (lst[i]>lst[i+1]):   #Если i-й элемент списка больше последующего за ним, то..."""
#                x=lst[i]            # кладём ссылку на обьект, а именно значение i-го элемента 
                                    # постоянную переменную х.
                                    #Если не использовать эту переменную, то при присваивании нового значения 
                                    # мы потеряем текущее...
#                lst[i]=lst[i+1]     #  ... после этого присваиваем текущему элементу значение следующего
                                    # (значение i+1 элемента) ---> i-й элемент.
#                lst[i+1]=x          # ссылку из переменной х присваиваем (i+1)
#        m=m-1                       # элемент с макс. значением оказался в конце списка. Поэтому далее рассматриваем список
                                    #без последнего элемента
#    return result
#lst = [14, 8, 3, 1, 89, 2, 45]
#print(lst)
#print(bubble_sort(lst))
#lst = [0.14, 0.8, 0.3, 0.1, 0.89, 0.2, 0.45]
#print(lst)
#?print(bubble_sort(lst))

#li = [5,2,7,4,0,9,8,6] 
#n = 0 #Задаём стартовый аргумент списка. Проверка начнётся с 0го элемента.
#while n < len(li):                              """Начинается перебор списка, начиная с нулевого,
#                                                каждый раз за цикл прибавляя единицу, до тех пор,
#                                                пока аргумент не сравнится с числом, равным количеству элементов списка (len())."""
#     for i in range(len(li)-1):                 """ """
##          if li[i] > li[i+1]:                   """ """
#               li[i] = li[i+1]                  """ """
#               li[i+1] = li[i]                  """ """
#     n += 1                                     """ """
#print(li)

#a = [1,4,6,1,8,5,3]
#print(a)
#m = len(a) - 1
#while m>0:
#    for i in range(m):
#        if (a[i] > a[i+1]):
#            x = a[i]
#            a[i] = a[i+1]
#            a[i+1] = x
#    m=m-1
#print(a)
#
#def average(lst):
#    c = sum(lst)/len(lst)
#    return round(c, 3) 
#lst = [14, 8, 3, 1, 89, 2, 45]
#print(average(lst))
#lst = [0.14, 0.8, 0.3, 0.1, 0.89, 0.2, 0.45]
#print(average(lst))
