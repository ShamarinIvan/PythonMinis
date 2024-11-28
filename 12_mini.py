def coroutine(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		next(result)
		return result

	return wrapper

@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)

def storage1():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)
def test():
	try:
		norm_storage = storage()
		print(norm_storage.send(42))
		print(norm_storage.send(42))
	except TypeError:
		print("Doesnt work(")
	finally:
		print("it works)")
	try:
		silly_storage = storage1()
		print(silly_storage.send(42))
		print(silly_storage.send(42))
	except TypeError:
		print("doesnt work(")
if __name__ == '__main__':
	test()
