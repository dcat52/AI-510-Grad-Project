import util
import qTools, dTools
import perceptron
import math as m

def featureExtractor(dataList):
    features = util.Counter()
    #features['AVG'] = 1.0*sum(dataList)/len(dataList)
    #features['SUM'] = sum(dataList)
    #features['MIN'] = min(dataList)
    #features['MAX'] = max(dataList)
    features['RNG'] = max(dataList)-min(dataList)
    temp = 0.0
    for x in dataList:
    	temp+=m.pow(x,2)

    features['RMS'] = m.pow(temp,.5)
    return features

def runClassifier(q,qData, iterCount):
    featureFunction = featureExtractor

    rawTrainingData = []
    for datum in qData._trainData:
        rawTrainingData.append(datum._data)

    trainingLabels = []
    for datum in qData._trainData:
        trainingLabels.append(datum._label)

    rawTestData = []
    for datum in qData._testData:
        rawTestData.append(datum._data)

    testLabels = []
    for datum in qData._testData:
        testLabels.append(datum._label)
    # Extract features
    print "Extracting features..."
    trainingData = map(featureFunction, rawTrainingData)
    testData = map(featureFunction, rawTestData)

    #print trainingData
    #print rawTrainingData
    #for d in qData._trainData:
    #    print d

    classifier = perceptron.PerceptronClassifier(list(q._labelSet), iterCount)
    # Conduct training and testing

    #print "---------------------"
    print "Training..."
    classifier.train(trainingData, trainingLabels)

    print "Testing..."
    guesses = classifier.classify(testData)
    correct = [guesses[i] == testLabels[i] for i in range(len(testLabels))].count(True)
    print str(correct), ("correct out of " + str(len(testLabels)) + " (%.1f%%).") % (100.0 * correct / len(testLabels))