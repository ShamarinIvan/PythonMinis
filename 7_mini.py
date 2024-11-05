def deprecated(since = None, will_be_removed = None):
    def decorator(f):
        def inner(*args, **kwargs):
            if(since is None and will_be_removed is None):
                print(f"Warning: function {f.__name__} is deprecated. It will be removed in future versions.")
            elif(since is None and will_be_removed is not None):
                print(f"Warning: function {f.__name__} is deprecated. It will be removed in version {will_be_removed}.")
            elif(since is not None and will_be_removed is None):
                print(f"Warning: function {f.__name__} is deprecated since version {since}. It will be removed in future versions.")
            else:
                print(f"Warning: function {f.__name__} is deprecated since version {since}. It will be removed in version {will_be_removed}.")
            return f(*args, **kwargs)
        return inner
    return decorator
@deprecated(will_be_removed = '4.2.0', since = '4.1.9')
def foo():
    print("Hello World\n")
foo()

@deprecated(since = '4.1.9')
def foo():
    print("Hello World\n")
foo()

@deprecated(will_be_removed = '4.2.0')
def foo():
    print("Hello World\n")
foo()

@deprecated()
def foo():
    print("Hello World\n")
foo()
