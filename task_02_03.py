def average(lst):
    c = sum(lst)/len(lst)
    n = 3
    return round(c, n) 
lst = [14, 8, 3, 1, 89, 2, 45]
print(lst)
print(average(lst))
lst = [0.14, 0.8, 0.3, 0.1, 0.89, 0.2, 0.45]
print(lst)
print(average(lst))