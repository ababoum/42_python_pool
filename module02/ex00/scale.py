from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce
function = lambda x: x + 1
iterable = [1, 2, 3]

print(ft_map(function_to_apply = None, iterable = iterable))

try:
	list(ft_map(function_to_apply = None, iterable = iterable))
except:
	print("ERROR")

print("*" * 42)

print(ft_filter(function_to_apply = None, iterable = iterable))

try:
	list(ft_filter(function_to_apply = None, iterable = iterable))
except:
	print("ERROR")

print("*" * 42)

try:
	ft_reduce(None, iterable = iterable)
except:
	print("ERROR")

try:
	ft_reduce(function, None)
except:
	print("ERROR")


print("=" * 42)

print(list(ft_map(lambda x: x + 2, [])))
print(list(ft_map(lambda x: x + 2, [1])))
print(list(ft_map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
print(list(ft_filter(lambda x: x <= 1, [])))
print(ft_reduce((lambda x, y: x + y), [1]))
print(ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]))

