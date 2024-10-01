class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x = value  # Directly assign the value to self._x



foo = Foo(10)
print(Foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)