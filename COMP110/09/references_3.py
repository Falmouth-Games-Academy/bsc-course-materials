class X:
    def __init__(self, value):
        self.value = value

a = X(10)
b = X(10)
a.value = 20
print("a:", a.value)
print("b:", b.value)
