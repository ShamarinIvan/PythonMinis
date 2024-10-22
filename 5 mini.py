def asum(x,y):
    return x + y

def specialize(f, *first_args, **first_kwargs):
    def omniknight(*then_args, **then_kwargs):
        args = first_args+then_args
        kwargs = {**first_kwargs, **then_kwargs}
        return f(*args, **kwargs)
    return omniknight

if __name__ == "__main__":
    assert(specialize(asum, 6)(13)) == 19
    assert(specialize(asum, 0, 8)()) == 8
    assert(specialize(asum)(4, y = 4)) == 8
