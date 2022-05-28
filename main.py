import operator
import pandas as pd
import math
import random
data_records = pd.read_csv(r'cardata.csv')

data_records.columns = ['buying','maint','doors','persons','lug_boot','safety','classes']
data_records.buying.replace(('vhigh','high','med','low'),(1,2,3,4), inplace=True)
data_records.maint.replace(('vhigh','high','med','low'),(1,2,3,4), inplace=True)
data_records.doors.replace(('2','3','4','5more'),(1,2,3,4), inplace=True)
data_records.persons.replace(('2','4','more'),(1,2,3), inplace=True)
data_records.lug_boot.replace(('small','med','big'),(1,2,3), inplace=True)
data_records.safety.replace(('low','med','high'),(1,2,3), inplace=True)
#data_records.classes.replace(('unacc','acc','good','vgood'),(1,2,3,4), inplace=True)
#print (data_records)

#dataset = []
#for i in range(0, len(data_records)):
#   dataset.append([((data_records.values[i, j])) for j in range(0,7)])

#training_set = []
#test_set = []
#split = 0.75
#for x in range(len(dataset) - 1):
#	for y in range(6):
#		dataset[x][y] = float(dataset[x][y])
#	if random.random() < split:
#		training_set.append(dataset[x])
#	else:
#		test_set.append(dataset[x])



seventyfive= (int)(len(data_records)*0.75)

training_set = []
for i in range(0, seventyfive-1):
   training_set.append([((data_records.values[i, j])) for j in range(0,7)])

test_set = []
for n in range(seventyfive-1, len(data_records)):
    test_set.append([((data_records.values[n, k])) for k in range(0,7)])


def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)



def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def make_predictions(neighbors):
	majority = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in majority:
			majority[response] += 1
		else:
			majority[response] = 1
	sortedVotes = sorted(majority.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]


def calculate_Accuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] in predictions[x]:
			correct = correct + 1

	return (correct / float(len(testSet)) * 100)

predictions=[]

input_k = int(input("Enter k:"))

for x in range(len(test_set)):
	neighbors = getNeighbors(training_set, test_set[x], input_k)
	#print(neighbors)
	result = make_predictions(neighbors)
	predictions.append(result)
	print('> predicted=' + repr(result) + ', actual=' + repr(test_set[x][-1]))

accuracy = calculate_Accuracy(test_set, predictions)
print('Accuracy: ' + repr(accuracy) + '%')


