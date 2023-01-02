# The 2D array is structured is like a grid structured into 
# rows and columns 
# Here, the 2D array would be built as an array of arrays
# Here, the array subscript will be accessed by [i, j] because i and j which are
# the rows and columns via a tuple representation in the __setitem__ magic method.

from array1D import Array1D

class Array2D:
	def __init__(self, nrows, ncols):
		assert int(nrows) == nrows and int(ncols) == ncols, "Rows and Columns must be integers"
		assert nrows > 0 and ncols > 0, "Rows or Column sizes too small and must be greater than zero"
		self._nrows = nrows
		self._ncols = ncols

		self._theRow = Array1D(nrows)

		for i in range(nrows):
			self._theRow[i] = Array1D(ncols)

	def __setitem__(self, indexTuple, value):
		assert len(indexTuple) == 2, "The index values to be subscripted must be 2"
		row, col = indexTuple
		assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols()

		self._theRow[row][col] = value


	def __getitem__(self, indexTuple):
		assert len(indexTuple) == 2, "The index values to be subscripted must be 2"
		row, col = indexTuple
		assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols()

		return self._theRow[row][col]

	def display(self):
		display_list = []
		for arrayStruct in self._theRow.display():
			display_list.append(arrayStruct.display())
		return display_list


	def numCols(self):
		return len(self._theRow[0])

	def numRows(self):
		return len(self._theRow)

	def clear(self, value):
		for i in range(self.numRows()):
			for j in range(self.numCols()):
				self._theRow[i][j] = value



# Solve for the averages of 
# the students in the exam file

file = open("exam.txt", "r")
numStudents = int(file.readline().strip())
numExam = int(file.readline().strip())

arr = Array2D(numStudents, numExam)

i = 0
for line in file:
	grades = line.strip().split()
	for j in range(len(grades)):
		arr[i, j] = int(grades[j])
	i += 1
	







