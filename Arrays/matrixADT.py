from array2D import Array2D

class Matrix:
	def __init__(self, nrows, ncols):
		self._theGrid = Array2D(nrows, ncols)
		self._theGrid.clear(0)

	def numCols(self):
		return self._theGrid.numCols()

	def numRows(self):
		return self._theGrid.numRows()

	def clear(self, value):
		self._theGrid.clear(value)

	def __getitem__(self, ndxTuple):
		row, col = ndxTuple
		return self._theGrid[row, col]

	def display(self):
		return self._theGrid.display()

	def __setitem__(self, ndxTuple, scalarValue):
		row, col = ndxTuple
		self._theGrid[row, col] = scalarValue

	def scaleBy(self, scalar):
		for i in range(self.numRows()):
			for j in range(self.numCols()):
				self._theGrid[i, j] *= scalar

	def __add__(self, rhsMatrix):
		# In order to perform an addition operation both matrices rows and columns must be equal
		assert rhsMatrix.numCols() == self.numCols() and \
		rhsMatrix.numRows() == self.numRows(), "The set matrices given cannot perform addition operation \
		because the number of rows and columns are not equal in both matrices"

		newMatrix = Matrix(self.numRows(), self.numCols())

		for i in range(self.numRows()):
			for j in range(self.numCols()):
				newMatrix[i, j] = self._theGrid[i, j] + rhsMatrix[i, j]
		return newMatrix
		

	def __sub__(self, rhsMatrix):
		# In order to perform an substraction operation both matrices rows and columns must be equal
		assert rhsMatrix.numCols() == self.numCols() and \
		rhsMatrix.numRows() == self.numRows(), "The set matrices given cannot perform subtraction operation because the number of rows and columns are not equal in both matrices"

		newMatrix = Matrix(self.numRows(), self.numCols())

		for i in range(self.numRows()):
			for j in range(self.numCols()):
				newMatrix[i, j] = self._theGrid[i, j] - rhsMatrix[i, j]
		return newMatrix

	def __mul__(self, rhsMatrix):
		assert self.numCols() == rhsMatrix.numRows(), "The number of nrows and ncols are incompatible"
		newMatrix = Matrix(rhsMatrix.numCols(), rhsMatrix.numCols())

		for i in range(self.numRows()): # (0, 3)
			for j in range(rhsMatrix.numCols()): # (0, 3)
				for k in range(rhsMatrix.numRows()): # (0, 2)
					# newMatrix[i, j] += ( self[i, k] * rhsMatrix[k, j] )
					print(f"i = {i} ", f"j = {j} ", f"k = {k} ")
					newMatrix[i, j] = newMatrix[i, j] + ( self[i, k] * rhsMatrix[k, j] )
		return newMatrix
	

	def transpose(self):
		# Return a new matrix where the rows are columns and the columns are rows
		matrix = self._theGrid
		col = self.numCols()
		row = self.numRows()
		newMatrix = Matrix(col, row)
		return newMatrix




# matrix[0, 0] = firstMatrix[0, 0] * secondMatrix[0, 1]



# matrix1 = Matrix(3, 2)
# matrix1[0,0] = 0
# matrix1[0,1] = 1
# matrix1[1,0] = 2
# matrix1[1,1] = 3
# matrix1[2,0] = 4
# matrix1[2,1] = 5

# matrix2 = Matrix(2, 3)
# matrix2[0,0] = 6
# matrix2[0,1] = 7
# matrix2[0,2] = 8
# matrix2[1,0] = 9
# matrix2[1,1] = 1
# matrix2[1,2] = 0

# print(matrix1.display())
# print(matrix2.display())
# matrix3 =   matrix1 * matrix2
# print(matrix3.display())
# file = open("exam.txt", "r")
# numStudents = int(file.readline().strip())
# numExam = int(file.readline().strip())

# matrix1 = Matrix(numStudents, numExam)

# i = 0
# for line in file:
# 	grades = line.strip().split()
# 	for j in range(len(grades)):
# 		matrix1[i, j] = int(grades[j])
# 	i += 1


# print(matrix1.display())
# print(matrix1.transpose().display())


