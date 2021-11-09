class X:
    pass

foo = X()
foo.x = foo
foo.y = "Hello"

print(foo.x.x.x.x.x.y)
