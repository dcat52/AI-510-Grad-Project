# dataTools

import csv, random
import questionTools as qTools

class dataTotal:
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

class datum:
	def __init__(self, data, label, dType=None):
		self._data = data
		self._label = label
		self._type = dType

	def __str__(self):
		return "data: %s\tlabel:%s" % (self._data, self._label)

class dataQuestion:
	def __init__(self, q, trainRatio):
		self._q = q
		self._trainRatio = trainRatio

		self._trainCount = 0

		self._trainData = []
		self._testData = []

		self.splitTrainAndTest()

		#print "train data:", len(self._trainData)
		#print "test data:", len(self._testData)

	def splitTrainAndTest(self):
		tempData = self._q._data[:]

		random.shuffle(tempData)
		dataCount = len(tempData)

		self._trainCount = int(dataCount * self._trainRatio)

		self._trainData = tempData[:self._trainCount]
		self._testData = tempData[self._trainCount:]

		assert dataCount == len(self._trainData) + len(self._testData)

		#print "\nTEST DATA:"
		#for d in self._testData:
		#	print "\t",d

	def reshuffle(self):
		self.splitTrainAndTest()