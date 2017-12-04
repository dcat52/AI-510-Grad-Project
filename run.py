import questionTools as qTools
import dataTools as dTools
import aiTools

# define the question # and question column set
problem = 1

csv = 'project510Data.csv'

dataTotal = dTools.dataTotal(csv)

q = qTools.Question(problem)
q.getInputDataAndLabels(dataTotal._dataList)

dataQ = dTools.dataQuestion(q, 0.85)

classifier = aiTools.classifier(q, dataQ, aiTools.featureExtractor, 100)
classifier.prepDataTrain()
# Conduct training and testing

#print "---------------------"
print "Training..."
classifier.train()
classifier.test()