import numpy


class NumpyCreator:

	def __init__(self) -> None:
		pass

	def from_list(self, lst):
		numpy.warnings.filterwarnings('ignore', category=numpy.VisibleDeprecationWarning)
		if not isinstance(lst, list):
			return None
		len_item = 0
		if lst:
			len_item = len(lst[0])
		if any(len(item) != len_item for item in lst):
			return None
		return numpy.array(lst)

	def from_tuple(self, tpl):
		if not isinstance(tpl, tuple):
			return None
		len_item = 0
		if tpl:
			len_item = len(tpl[0])
		if any(len(item) != len_item for item in tpl):
			return None
		return numpy.array(tpl)

	def from_iterable(self, itr):
		return numpy.array(itr)

	def from_shape(self, shape, value=0.0):
		if any(not isinstance(item, int) or item < 0 for item in shape):
			return None
		return numpy.full(shape, value)

	def random(self, shape):
		if any(not isinstance(item, int) or item < 0 for item in shape):
			return None
		return numpy.random.rand(*shape)

	def identity(self, n):
		if not isinstance(n, int) or n < 0:
			return None
		return numpy.identity(n)


if __name__ == "__main__":
	npc = NumpyCreator()
	print(repr(npc.from_list([[1,2,3],[6,3,4]])))
	print('*' * 25)
	# Output :
	# array([[1, 2, 3],
	# [6, 3, 4]])
	print(npc.from_list([[1,2,3],[6,4]]))
	print('*' * 25)
	# Output :
	# None
	print(repr(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]])))
	print('*' * 25)
	# Output :
	# array([['1','2','3'],
	# ['a','b','c'],
	# ['6','4','7'], dtype='<U21'])
	print(repr(npc.from_list(((1,2),(3,4)))))
	print('*' * 25)
	# Output :
	# None
	print(repr(npc.from_tuple(("a", "b", "c"))))
	print('*' * 25)
	# Output :
	# array(['a', 'b', 'c'])
	print(repr(npc.from_tuple(["a", "b", "c"])))
	print('*' * 25)
	# Output :
	# None
	print(repr(npc.from_iterable(range(5))))
	print('*' * 25)
	# Output :
	# array([0, 1, 2, 3, 4])
	shape=(3,5)
	print(repr(npc.from_shape(shape)))
	print('*' * 25)
	# Output :
	# array([[0, 0, 0, 0, 0],
	# [0, 0, 0, 0, 0],
	# [0, 0, 0, 0, 0]])
	print(repr(npc.random(shape)))
	print('*' * 25)
	# Output :
	# array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],
	# [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
	# [0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])
	print(npc.identity(4))
	print('*' * 25)
	# Output :
	# array([[1., 0., 0., 0.],
	# [0., 1., 0., 0.],
	# [0., 0., 1., 0.],
	# [0., 0., 0., 1.]])

	print('=' * 42)
	
	print(repr(npc.from_list([[],[]])))
	print('*' * 25)

	print(repr(npc.from_list([[1,2,3],[6,3,4],[8,5,6]])))
	print('*' * 25)

	print(repr(npc.from_tuple(("a","b","c"))))
	print('*' * 25)

	print(repr(npc.from_iterable(range(5))))
	print('*' * 25)
	
	print(repr(npc.from_shape((0, 0))))
	print('*' * 25)

	print(repr(npc.from_shape((3, 5))))
	print('*' * 25)

	print(repr(npc.random((3, 5))))
	print('*' * 25)

	print(repr(npc.identity(4)))
	print('*' * 25)


	print("=" * 21 + "ERROR MANAGEMENT" + "=" * 21)

	print(npc.from_list("toto"))
	print(npc.from_list([[1,2,3],[6,3,4],[8,5,6,7]]))
	print(npc.from_tuple(3.2))
	print(npc.from_tuple(((1,5,8),(7,5))))
	print(npc.from_shape((-1, -1)))
	print(npc.identity(-1))