import sys


print(sys.__stdin__)

class New_Input(object):
    def __stdin__(self, objects):
        return self.objects

new = New_Input()
print(new)

a = 'awer'

print(sys.stdin.read(2))
