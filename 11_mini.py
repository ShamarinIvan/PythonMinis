def cycle(iterable):
	saved = []
	for element in iterable:
		yield element
		saved.append(element)
	while saved:
		for element in saved:
			yield element
def take(cycle, n):
	array = []
	count = 0
	for el in cycle:
		array.append(el)
		count += 1
		if count == n:
			return array
def chain(*args):
	for el in args:
		for obj in el:
			yield obj
my_list = [43, 13, 7]
print(take(cycle([1,2,3]),5))
print(list(chain([1,2,3], ['a', 'b'], my_list)))

