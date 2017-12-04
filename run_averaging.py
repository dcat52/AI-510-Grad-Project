import questionTools as qTools
import dataTools as dTools
import aiTools

def main():
	# define the question # and question column set
	problem = 2

	csv = 'project510Data.csv'

	dataTotal = dTools.dataTotal(csv)

	q = qTools.Question(problem)
	q.getInputDataAndLabels(dataTotal._dataList)

	trainToTestRatio = 0.9

	dataQ = dTools.dataQuestion(q, trainToTestRatio)

	nRuns = 10

	classifier = aiTools.classifier(q, dataQ, aiTools.featureExtractor, maxIter)

	avgNruns(dataQ, classifier, nRuns)

def avgNruns(dataQ, classifier, n):
	tests = []
	for i in range(n):
		classifier.prepDataTrain()
		classifier.train()
		tests.append(classifier.test())
		#print "\tRun %d accuracy was: %.2f%s" % (i, tests[len(tests)-1]*100, "%")
		classifier.reset()
		dataQ.reshuffle()

	avg = sum(tests)/len(tests)
	print "Over %d runs, accuracy was: %.2f%s" % (len(tests), avg*100, "%")
	return avg


if __name__=="__main__":
	main()