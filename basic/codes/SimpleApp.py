from pyspark import SparkContext
import sys
from pyspark.mllib.clustering import LDA, LDAModel
from pyspark.mllib.linalg import Vectors
from pyspark.sql import Row
#!/usr/bin/env python
#-*-coding:utf-8-*-

def func(x):
	result=[]
	index = x[0]
	for i in x[1]:
		result.append(((index, i),1))
	return result
def ok(v):
	k = ""
	for i in v:
		k = k + str(i[1]) + " "
	return k
def f(x,y):
	if y==None:
		return x
	else:
		return x+y
def d(x,numberoftweets):
	result=[]
	for i in range(numberoftweets):
		a= ((i,x),0)
		result.append(a)
	return result

def main():
	p = sys.argv[1]
	logFile = "data/" + p + ".txt"
	sc = SparkContext("local", "simpleApp")
	data = sc.textFile(logFile).cache()
	numberoftweets = data.count()
	words = data.flatMap(lambda x: x.split(" ")).distinct()
	word_list = words.collect()
	words = words.flatMap(lambda x:d(x,numberoftweets))
	data = data.zipWithIndex().map(lambda (x,y): (y,x.split(" ")))
	wc = data.flatMap(lambda x: func(x)).groupByKey().mapValues(lambda x: len(x))
	mat = words.leftOuterJoin(wc).map(lambda (x,y):  (x[0],(x[1], f(y[0],y[1])))).groupByKey().sortByKey().mapValues(lambda x:list(x)).mapValues(lambda x: ok(x))
	parsedData = mat.mapValues(lambda line: Vectors.dense([float(x) for x in line.strip().split(' ')])).map(lambda (x,y): [x,y])
	# Index documents with unique IDs
	corpus = parsedData.cache()

	# Cluster the documents into three topics using LDA
	ldaModel = LDA.train(corpus, k=3)
	# Output topics. Each is a distribution over words (matching word count vectors)
	topics = ldaModel.topicsMatrix()
	topics_dict={}
	for topic in range(3):
		k = "Topic "+ str(topic)
		topics_dict[k] = {}
		for word in range(0, ldaModel.vocabSize()):
			topics_dict[k][str(topics[word][topic])] = word_list[word]
	path = "data/" + p + "results.txt"
	json = open(path, 'w')

	for i in topics_dict.keys():
		counter=0
		z = sorted(topics_dict[i],reverse=True)
		for l in z:
			if counter == 7: break
			ww = topics_dict[i][l] + " "
			counter+=1
			json.write(ww)
		json.write("\n")
	json.close()

	# Start Here
	#logData = logData.map(lambda x: (x,"Spark has been used!"))
	#result = logData.collect()

	# No need
	#for element in result:

		# Check whether all chracters are ASCII
	#    try:
	#        print element[0] + " - " + element[1]
	#    except:
	#        pass

if __name__ == "__main__":
	main()
