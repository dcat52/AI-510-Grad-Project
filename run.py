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

	dataQ = dTools.dataQuestion(q, 0.90)

	nRuns = 10
	
	allRuns = []
	print "----"
	for ratio in range(950, 1000, 50):
		dataQ = dTools.dataQuestion(q, 1.0*ratio/1000)
		for maxIter in range(100,300,25):
			print "RATIO:", 1.0*ratio/1000
			print "MAX ITER: %d" % (maxIter)
			classifier = aiTools.classifier(q, dataQ, aiTools.featureExtractor, maxIter)

			allRuns.append((avgNruns(dataQ, classifier, nRuns),1.0*ratio/1000,maxIter))
			print "--"
		print "----"

	allRuns.sort()
	print "TOP 15 RUNS:"
	for x in allRuns[-14:][::-1]:
		print x


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