# questionTools
import dTools

class Question:
	def __init__(self, problem):
		self._problem = problem
		self._data = []
		self._labelSet = set()
		self._columns = lookupColumns(self._problem)

		print "running '%s' with columns '%s'." % (self._problem, self._columns)


	def getInputDataAndLabels(self, dataList):

		removedDataCount = 0
		labelCell = self._columns[len(self._columns)-1]

		for i, dataRow in enumerate(dataList):

			tempInputs = []
			validRow = True

			for j in self._columns[:-1]:
				tempInputs.append(dataRow[j])

				if dataRow[j] < -2.0:
					removedDataCount += 1
					tempInputs = []
					validRow = False
					break

			if validRow:
				datum = dTools.datum(tempInputs, dataRow[labelCell])
				self._data.append(datum)
				self._labelSet.add(dataRow[labelCell])

		print "Removed data row count:", removedDataCount
		print "Remaining data row count:", len(self._data)
		print "Number of unique labels:", len(self._labelSet)

		assert removedDataCount + len(self._data) == len(dataList)


def lookupColumns(_problem):
	questions = {}
	questions['q1'] = [2,3,4,5,10] # 			10%
	questions['q2'] = [2,3,4,10] # 				10%
	questions['q3'] = [0,1,2,3,4,5,10] # 		10%
	questions['q4'] = [2,3,4,5,6,9,10] # 		10%

	questions['q5'] = [2,3,4,5,6,9,11] # 		5%
	questions['q6'] = [0,1,2,3,4,5,6,9,10,11] # 5%

	return questions[_problem]