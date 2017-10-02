x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
x31 = x3-x1
if x31 > 0:
    x31 = x31
else:
    x31 = x31*(-1)
y31 = y3 - y1
if y31 > 0:
    y31 = y31
else:
    y31 = y31*(-1)
x21 = x2 - x1
if x21 > 0:
    x21 = x21
else:
    x21 = x21*(-1)
y21 = y2 - y1
if y21 > 0:
    y21 = y21
else:
    y21 = y21*(-1)
x32 = x3 - x2
if x32 > 0:
    x32 = x32
else:
    x32 = x32*(-1)
y32 = y3 - y2
if y31 > 0:
    y32 = y32
else:
    y32 = y32*(-1)
if (x31)**2+(y31)**2 == (x21)**2+(y21)**2+(x32)**2+(y32)**2:    
    print('Прямоугольный')
elif (x31)**2+(y31)**2 + (x32)**2+(y32)**2 == (x21)**2+(y21)**2:
    print('Прямоугольный')
elif (x31)**2+(y31)**2 + (x21)**2+(y21)**2 == (x32)**2+(y32)**2:
    print('Прямоугольный')
#if (x3-x1)**2+(y3-y1)**2 == (x2-x1)**2+(y2-y1)**2+(x3-x2)**2+(y3-y2)**2:
else:
    print('Непрямоугольный')