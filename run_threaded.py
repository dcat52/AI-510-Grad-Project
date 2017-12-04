import time, sys, multiprocessing

import questionTools as qTools
import dataTools as dTools
import aiTools

def avgNruns(dataQ, classifier, problem, return_dict, i):
	#runs = []
	classifier.reset()
	dataQ.reshuffle()
	classifier.prepDataTrain()
	classifier.train()
	v = classifier.test()
	print "\tAccuracy was: %.2f%s" % (v*100, "%")
	return_dict[i] = v

	

def main(problem, dataTotal):

	import questionTools as qTools
	import dataTools as dTools
	import aiTools 

	q = qTools.Question(problem)
	q.getInputDataAndLabels(dataTotal._dataList)
	dataQ = dTools.dataQuestion(q, 0.90)
	
	classifier = aiTools.classifier(q, dataQ, aiTools.featureExtractor, 200)

	manager = multiprocessing.Manager()
	return_dict = manager.dict()
	tasks = manager.Queue()
	num_processes = 10
	pool = multiprocessing.Pool(num_processes)
	proc = []
	for i in range(num_processes):
		process_name = 'Proc%i' % i
		p = multiprocessing.Process(target=avgNruns, args=(dataQ, classifier, problem, return_dict, i))
		proc.append(p)
		p.start()

	for p in proc:
		p.join()

	runs = return_dict.values()
	avg = 1.0*sum(runs)/len(runs)
	print "\nPROBLEM %d\nOver %d runs, accuracy averaged: %.2f%s\n" % (problem, len(runs), avg*100, "%")

csv = 'project510Data.csv'

dataTotal = dTools.dataTotal(csv)

manager = multiprocessing.Manager()
tasks = manager.Queue()
num_processes = 1
pool = multiprocessing.Pool(num_processes)

processes = []
for i in range(num_processes):
	process_name = 'P%i' % i
	new_process = multiprocessing.Process(target=main, args=(i+2, dataTotal,))
	new_process.daemon = False
	processes.append(new_process)
	new_process.start()

alive = True
while alive:
	try:
		alive = False
		for p in processes:
			if p.is_alive():
				alive = True
		if not alive:
			sys.exit()
		time.sleep(2)

	except (KeyboardInterrupt, SystemExit):
		alive = False
		sys.exit()