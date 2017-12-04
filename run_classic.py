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

	classifier.prepDataTrain()
	classifier.train()
	tests.append(classifier.test())

if __name__=="__main__":
	main()