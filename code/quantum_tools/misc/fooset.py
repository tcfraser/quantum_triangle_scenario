class Fooset(set):
    def __init__(self, s=(), foo=None):
        super(Fooset,self).__init__(s)
        if foo is None and hasattr(s, 'foo'):
            foo = s.foo
        self.foo = foo

    @classmethod
    def _wrap_methods(cls, names):
        def wrap_method_closure(name):
            def inner(self, *args):
                result = getattr(super(cls, self), name)(*args)
                if isinstance(result, set) and not hasattr(result, 'foo'):
                    print(result)
                    result = cls(result, foo=self.foo)
                    print(result)
                return result
            inner.fn_name = name
            setattr(cls, name, inner)
        for name in names:
            wrap_method_closure(name)

Fooset._wrap_methods(['__ror__', 'difference_update', '__isub__',
    'symmetric_difference', '__rsub__', '__and__', '__rand__', 'intersection',
    'difference', '__iand__', 'union', '__ixor__',
    'symmetric_difference_update', '__or__', 'copy', '__rxor__',
    'intersection_update', '__xor__', '__ior__', '__sub__',
])

if __name__ == '__main__':
    A = Fooset(('A', 'B', 'C'))
    B = Fooset(('B', 'C'))
    print(A)
    print(B)
    print(A - B)