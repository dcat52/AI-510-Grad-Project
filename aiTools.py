import questionTools as qTools
import dataTools as dTools
import util
import math as m

def featureExtractor(dataList):
    features = util.Counter()
    features['AVG'] = 1.0*sum(dataList)/len(dataList)
    features['SUM'] = sum(dataList)
    features['MIN'] = min(dataList)
    features['MAX'] = max(dataList)
    features['RNG'] = max(dataList)-min(dataList)
    temp = 0.0
    for x in dataList:
        temp+=m.pow(x,2)

    features['RMS'] = m.pow(temp,.5)
    return features

class classifier:
    def __init__(self, q, dataQ, featureFunction, iterations=100):
        self._q = q
        self._dataQ = dataQ
        self._legalLabels = list(q._labelSet)
        self._featureFunction = featureFunction
        self._iterations = iterations

        self.weights = {}
        for label in self._legalLabels:
            self.weights[label] = util.Counter()

        self._trainingData = None
        self._trainingLabels = None

        self._testData = None
        self._testLabels = None

    def prepDataTrain(self):
        rawTrainingData = []
        for datum in self._dataQ._trainData:
            rawTrainingData.append(datum._data)

        self._trainingLabels = []
        for datum in self._dataQ._trainData:
            self._trainingLabels.append(datum._label)

        rawTestData = []
        for datum in self._dataQ._testData:
            rawTestData.append(datum._data)

        self._testLabels = []
        for datum in self._dataQ._testData:
            self._testLabels.append(datum._label)

        # Extract features
        self._trainingData = map(self._featureFunction, rawTrainingData)
        self._testData = map(self._featureFunction, rawTestData)

    def reset(self):
        self.weights = {}
        for label in self._legalLabels:
            self.weights[label] = util.Counter()

    def getWeights(self):
        return self.weights

    def again(self):
        self.prepDataTrain()

    def train( self):
        trainingData = self._trainingData
        trainingLabels = self._trainingLabels

        for iteration in range(self._iterations):
            #print "Starting iteration ", iteration, "..."

            for i in range(len(trainingData)):

                datum = trainingData[i]
                trueLabel = trainingLabels[i]
                #print trueLabel
                prediction = self.classify([datum])[0] # [0] gets best guess

                if prediction != trueLabel:
                    self.weights[trueLabel] += datum
                    self.weights[prediction] -= datum


    def classify(self, data):
        #data = self._classHandler._testData

        guesses = []
        for d in data:
            vectors = util.Counter()
            for l in self._legalLabels:
                vectors[l] = self.weights[l] * d
            guesses.append(vectors.argMax())
        return guesses

    def test(self):
        testLabels = self._testLabels
        testData = self._testData

        guesses = self.classify(testData)
        correct = [guesses[i] == testLabels[i] for i in range(len(testLabels))].count(True)
        return (1.0 * correct / len(testLabels))
        #print str(correct), ("correct out of " + str(len(testLabels)) + " (%.1f%%).") % (100.0 * correct / len(testLabels))