from functools import wraps
def deprecated(function=None, since=None, will_be_removed=None):
    def decorator(f):
        @wraps(f)
        def inner(*args, **kwargs):
            name = f.__name__
            message = (f"Warning: function {name} is deprecated{f' since {since}' if since else ''}. It will be removed in {f'version {will_be_removed}' if will_be_removed else 'future versions'}\n")
            print(message)
            return f(*args, **kwargs)
        return inner
    if function is None:
        return decorator
    else:
        return decorator(function)
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
