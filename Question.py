import csv

class Data:
	def __init__(self, csv):
		self._csv = csv
		self._dataList = []
		self.readCSV()

	def readCSV(self):
		with open(self._csv, 'rb') as csvfile:
			csvReader = csv.reader(csvfile, delimiter=',')
			for row in csvReader:
				dataRow = [ float(s) for s in row]
				self._dataList.append(dataRow)

class Question:
	def __init__(self, problem):
		self._problem = problem
		self._inputData = []
		self._labelData = []
		self._labelSet = []
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
				self._inputData.append(tempInputs)
				self._labelData.append(dataRow[labelCell])

		self._labelSet = set(self._labelData)
		print "Removed data row count:", removedDataCount
		print "Remaining data row count:", len(self._inputData)
		print "Number of unique labels:", len(self._labelSet)

		assert len(self._inputData) == len(self._labelData)
		assert removedDataCount + len(self._inputData) == len(dataList)


def lookupColumns(_problem):
	questions = {}
	questions['q1'] = [2,3,4,5,10] # 			10%
	questions['q2'] = [2,3,4,10] # 				10%
	questions['q3'] = [0,1,2,3,4,5,10] # 		10%
	questions['q4'] = [2,3,4,5,6,9,10] # 		10%

	questions['q5'] = [2,3,4,5,6,9,11] # 		5%
	questions['q6'] = [0,1,2,3,4,5,6,9,10,11] # 5%

	return questions[_problem]