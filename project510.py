import csv
import numpy as np
import random
import pickle

dataList = [] # Empty list
dataDict = {}

with open('project510Data.csv', 'rb') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    for row in datareader:

        id = row[-1]
        dataVec = np.asarray([ float(s) for s in row])
        #print " >",id,"< ",dataVec.dtype,":",dataVec
        dataDict[id] = dataVec
        dataList.append(dataVec)


# We will access the data according to index into dataList
indices = range(0,len(dataList)) # a list of all valid indices
random.shuffle(indices)          # shuffle the list in place

numTrain = int(0.9*len(dataList))# Will use 90% for training
train = indices[:numTrain]  # Get 90% of shuffled indices for training
test  = indices[numTrain:]  # Use the remainder as a test class
#print "train=",train
#print " test=",test

# Example of writing a csv file using just the given data
with open('project510Train.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for ndx in sorted(train):
        # This prints out only 2 decimal places to keep lines reasonable length
        spamwriter.writerow(['{:.2f}'.format(x) for x in dataList[ndx]])

# I should hold out some of my training data for validation
with open('project510Test.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for ndx in sorted(test):
        spamwriter.writerow(['{:.2f}'.format(x) for x in dataList[ndx]])


# Below is an ill conceived attempt at classifying using a simple
# linear function of our input features.  It doesn't work, but illustrates
# many of the operations you will need.

# Sample of poor attempt at classifying using a simple linear function
W = np.array([0., 0., 0., 0., 0.]) # initial weights

# Define which columns we will select for input vector
columns = [0,2,4,6] # Column data to select for input vector

# Multiple passes through training data
for itr in range(0,20):
    random.shuffle(train) # randomize training input order
    #print "Weights at start=",W
    for ndx in train:
        sample = dataList[ndx]

        # Extract the relevant elements for this problem
        #  We get the first four elements from data and add a bias
        #print "sample data:",sample
        vec = np.transpose(np.append(sample[columns],[1.0]))
        #print "selection   :",vec

        if (any(vec < -2.)):
            # Skip any samples that have invalid data
            #print "Skipping", ndx
            continue
        label = sample[7]

        #print "vec=",vec
        val = np.dot(W,vec)
        err = label - val
        gradient = -err * vec # loss = 0.5*err*err
        W = W - 0.25*gradient
        #print " ",itr," ", ndx," : ",vec," label:",label," value: ",val, " err=",err, " grad=",gradient

    print "Weights at end = ",W

# Save the trained Weights and other variables for later use
pickle.dump( (W, 3.0, 4.0), open( "project510.pkl", "wb" ) )

# Toss our weights away to demonstrating loading from a pickle file
W = None

# Load in prior saved weights for use in classifier
W,three,four = pickle.load(open( "project510.pkl", "rb" ) )
print "Weights from pickle file = ",W

print "sample variables also loaded from pickle: three=", three, "four=", four

# Classify the test data
# NOTE: This is not a good attempt - you will do better!
loss = 0.0
labels = []
for ndx in test:
    sample = dataList[ndx]

    # Extract the relevant elements for this problem
    vec = np.append(sample[columns],[1.0]) # add a bias element
    vec = np.transpose(vec)
    label = sample[7]
    if (any(vec < -2.0)):
        labels.append(None)
        print "skipping test of ndx=",ndx," ID=",sample[12]
        continue  # Skip the rest of loop


    val = np.dot(W,vec)
    err = label - val
    print " ", ndx," ID ",sample[12]," : ",vec," label:",label," value: ",val, " err=",err
    loss = loss + 0.5*err*err
    labels.append(label)

print "labels=",labels
print "Total loss=",loss
