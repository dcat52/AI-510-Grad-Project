import util

import qTools, dTools

class PerceptronClassifier:
    """
    Perceptron classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "perceptron"
        self.max_iterations = max_iterations
        self.weights = {}
        for label in legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

        #print self.weights

    def setWeights(self, weights):
        assert len(weights) == len(self.legalLabels);
        self.weights = weights;

    def train( self, trainingData, trainingLabels):

        for iteration in range(self.max_iterations):
            #print "Starting iteration ", iteration, "..."

            for i in range(len(trainingData)):

                datum = trainingData[i]
                trueLabel = trainingLabels[i]
                #print trueLabel
                prediction = self.classify([datum])[0] # [0] gets best guess

                if prediction != trueLabel:
                    self.weights[trueLabel] += datum
                    self.weights[prediction] -= datum

        print self.weights

    def classify(self, data):
        guesses = []
        for datum in data:
            vectors = util.Counter()
            for l in self.legalLabels:
                vectors[l] = self.weights[l] * datum
            guesses.append(vectors.argMax())
        return guesses

