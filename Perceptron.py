import util

class Perceptron:
	def __init__(self, iterations, ds):
		"""
		iterations: number of runs to classify data on
		ds: dataSet obj containing lists of datums and labels
		"""

		self._iterations = iterations
		self._data = ds._datums
		self._labels = ds._labels
		self._weights = util.Counter()
		self._features = util.Counter()

	def classify(self, datum):
		"""
		"""
		values = datum._values
		label = datum._label

		for l in self._labels:
			self.featureExtractor(datum)*self._weights