import ctypes

# The 1D array ADT is a data structure that stores a limited number (size) of elements.
# It is unlike the Python list structure because it can not take more values than those
# specified and has a limited number of operations. This data structure is used when one
# do not require wastage of space.

# Here the ArrayADT is implemented in the hardware level using the ctypes module 
# that gives Python a C level storage capababilty.

class Array1D:
	# Here we initialize the array structure with the 
	# presumed limited size or length
	def __init__(self, size):
		assert int(size) == size, "Size must be an integer"
		assert size > 0, "Size is too small and must be greater than zero"

		self._size = size
		PyArray = ctypes.py_object * size

		self._elements = PyArray()

		# Here, initialize the clear() method because we need all our 
		# elements in our C structure to be initalized as None.
		self.clear(None)

	# In order to get an item from the elements in this struture, we
	# must first ensure the index is not less than zero and it's as well
	# not greater than the length or size of the array.
	def __getitem__(self, index):
		assert int(index) == index, "Index must be an integer"
		assert index >= 0 and index < self._size, "Index is out of range"
		return self._elements[index]

	def __setitem__(self, index, value):
		assert int(index) == index, "Index must be an integer"
		assert index >= 0 and index < self._size, "Index is out of range"
		self._elements[index] = value

	def __len__(self):
		return self._size

	def __iter__(self):
		# An interator class that would in some way 
		# behave like a real iterator
		return _ArrayIterator(self._elements)

	def clear(self, value):
		for i in range(len(self._elements)):
			self._elements[i] = None

	# The `display` method is only used to display the 
	# array ADT for the purpose of readability
	def display(self):
		display_list = []
		for item in self._elements:
			display_list.append(item)
		return display_list

	# The `pop` method receives an index argumant and asserts that the index provided
	# is null or it greater than or equal to zero and lesser than size
	# If index is not provided, the last item is turned to None
	# If index is provided, the value in the index position is turned to None
	def pop(self, index=None):
		assert index == None or (index >= 0 and index < len(self)), "Index is out of range"
		last_index = len(self._elements) - 1
		if index == None:
			self._elements[last_index] = None
		else:
			self._elements[index] = None


class _ArrayIterator:
	# The iterator class is initialized with the array reference
	# in order to perform iterator functionality on the array.
	def __init__(self, arrayRef):
		self._arrayRef = arrayRef
		self.currIndx = 0

	# Every iteration has an iter value which returns itself
	# This helps Python know that this value is iterable
	def __iter__(self):
		return self

	# next, on the other hand, helps go through each value one
	# after the other until it reaches the last value, 
	# and then a StopIteration error is raised
	def __next__(self):
		if self.currIndx < len(self._arrayRef):
			item = self._arrayRef[self.currIndx]
			self.currIndx += 1
			return item
		else:
			raise StopIteration



# Use the array ADT as follows:
arr = Array1D(7)
