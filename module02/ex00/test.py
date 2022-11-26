'''
Test examples for map, filter, and reduce recoded functions
'''

# Example 1:
from functools import reduce
from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
print(map(lambda dum: dum + 1, x))
# Output:
# <generator object ft_map at 0x7f708faab7b0> # The adress will be different
print(list(ft_map(lambda t: t + 1, x)))
print(list(map(lambda t: t + 1, x)))
# Output:
# [2, 3, 4, 5, 6]
print("*******************************************")
# Example 2:
print(ft_filter(lambda dum: not (dum % 2), x))
print(filter(lambda dum: not (dum % 2), x))
# Output:
# <generator object ft_filter at 0x7f709c777d00> # The adress will be different
print(list(ft_filter(lambda dum: not (dum % 2), x)))
print(list(filter(lambda dum: not (dum % 2), x)))
# Output:
# [2, 4]
print("*******************************************")
# Example 3:
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
print(reduce(lambda u, v: u + v, lst))
# Output:
# "Hello world"
lst = ['H']
print(ft_reduce(lambda u, v: u + v, lst))
print(reduce(lambda u, v: u + v, lst))
# Output:
# "H"
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ft_reduce(lambda u, v: u + v, lst))
print(reduce(lambda u, v: u + v, lst))
# Output:
# "55"
lst = [1]
print(ft_reduce(lambda u, v: u + v, lst))
print(reduce(lambda u, v: u + v, lst))
# Output:
# "1"

print("**********************************")

try:
    print(list(ft_filter('lala', 'lala')))
except Exception as e:
    print(repr(e))

try:
    print(list(filter('lala', 'lala')))
except Exception as e:
    print(repr(e))

print("**********************************")

try:
    print(list(ft_filter(lambda x: x + 1, 153)))
except Exception as e:
    print(repr(e))

try:
    print(list(filter(lambda x: x + 1, 153)))
except Exception as e:
    print(repr(e))

print("**********************************")

try:
    print(list(ft_map('lala', 'lala')))
except Exception as e:
    print(repr(e))

try:
    print(list(map('lala', 'lala')))
except Exception as e:
    print(repr(e))
    
print("**********************************")

try:
    print(list(ft_map(lambda x: x + 1, 153)))
except Exception as e:
    print(repr(e))

try:
    print(list(map(lambda x: x + 1, 153)))
except Exception as e:
    print(repr(e))
    
print("**********************************")

try:
    print(list(ft_reduce('lala', 'lala')))
except Exception as e:
    print(repr(e))

try:
    print(list(reduce('lala', 'lala')))
except Exception as e:
    print(repr(e))
    
print("**********************************")

try:
    print(list(ft_reduce(lambda x: x + 1, 153)))
except Exception as e:
    print(repr(e))

try:
    print(list(reduce(lambda x: x + 1, 153)))
except Exception as e:
    print(repr(e))

