import threading, time, sys

import questionTools as qTools
import dataTools as dTools
import aiTools

def avgNruns(dataQ, classifier, n, problem):
	tests = []
	for i in range(n):
		classifier.prepDataTrain()
		classifier.train()
		tests.append(classifier.test())
		#print "\tRun %d accuracy was: %.2f%s" % (i, tests[len(tests)-1]*100, "%")
		classifier.reset()
		dataQ.reshuffle()

	avg = 1.0*sum(tests)/len(tests)
	print "---\nPROBLEM %d\nOver %d runs, accuracy averaged: %.2f%s\n" % (problem, len(tests), avg*100, "%")


def main(problem, dataTotal):

	q = qTools.Question(problem)
	q.getInputDataAndLabels(dataTotal._dataList)
	dataQ = dTools.dataQuestion(q, 0.90)

	nRuns = 10
	
	classifier = aiTools.classifier(q, dataQ, aiTools.featureExtractor, 50)

	avgNruns(dataQ, classifier, 10, problem)

csv = 'project510Data.csv'

dataTotal = dTools.dataTotal(csv)

exitFlag = 0
class myThread(threading.Thread):
   	def __init__(self, name, problem, dataTotal):
		threading.Thread.__init__(self)
		self.name = name
		self.problem = problem
		self.dataTotal = dataTotal
		self.daemon = True

   	def run(self):
		print "Starting " + self.name
		main(self.problem, self.dataTotal )
		print "Exiting " + self.name

# Create new threads
thread1 = myThread("T1", 1, dataTotal)
thread2 = myThread("T2", 2, dataTotal)

# Start new Threads
thread1.start()
thread2.start()
threads = []
threads.append(thread1)
threads.append(thread2)
good = True
while good:
	try:
		if threading.activeCount() <= 1:
			good = False
		time.sleep(1)

	except (KeyboardInterrupt, SystemExit):
		good = False
		sys.exit()

	except:
		good = False
		sys.exit()