
a = int(input())
if a > 0:
    print(a)
else:
    try:
        raise ValueError
    except:
        print('ValueError')
#except:
#    print('privet')
