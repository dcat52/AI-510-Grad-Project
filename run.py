import qTools, dTools
import perceptron
import aiTools

# define the question # and question column set
problem = 'q1'

csv = 'project510Data.csv'

data = dTools.data(csv)

q1 = qTools.Question(problem)
q1.getInputDataAndLabels(data._dataList)

q1_data = dTools.qData(q1, 0.85)

aiTools.runClassifier(q1,q1_data, 100)
