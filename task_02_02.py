def bubble_sort(lst):
    result = lst                    #Результатом выполнение функции является список
    m = len(lst) - 1                #Определяем количество проходов по списку, как количество элементов списка -1.
                                    #-1 чтобы не превысить индекс списка после сравнения предпоследнего
                                    #элемента с последним
    while m>0:                      #Начинаем цикл, который будет продолжаться для всех m > 0, начиная с
                                    # m равным (блина списка - 1)
        for i in range(m):          #Выполнение цикла для каждого индекса i, начиная со значения 0,
                                    #т.е. с 1го элемента списка, до конца текущего списка
                                    #Количество проходов будет уменьшаться, т.к. каждый проход "выталкивает
                                    #максимальное значение на последнее место рассматриваемую позицию
                                    #Количество проходов будет каждый раз уменьшаться на 1 (m=m-1)
            if (lst[i]>lst[i+1]):   #Если i-й элемент списка больше последующего за ним, то..."""
                x=lst[i]            # кладём ссылку на обьект, а именно значение i-го элемента 
                                    # постоянную переменную х.
                                    #Если не использовать эту переменную, то при присваивании нового значения 
                                    # мы потеряем текущее...
                lst[i]=lst[i+1]     #  ... после этого присваиваем текущему элементу значение следующего
                                    # (значение i+1 элемента) ---> i-й элемент.
                lst[i+1]=x          # ссылку из переменной х присваиваем (i+1)
        m=m-1                       # элемент с макс. значением оказался в конце списка. Поэтому далее рассматриваем список
                                    #без последнего элемента
    return result
lst = [14, 8, 3, 1, 89, 2, 45]
print(lst)
print(bubble_sort(lst))
lst = [0.14, 0.8, 0.3, 0.1, 0.89, 0.2, 0.45]
print(lst)
print(bubble_sort(lst))