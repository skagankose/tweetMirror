from pyspark import SparkContext
import sys
from pyspark.mllib.clustering import LDA, LDAModel
from pyspark.mllib.linalg import Vectors
from pyspark.sql import SQLContext,Row
import os
from pyspark.ml.feature import CountVectorizer
#!/usr/bin/env python
#-*-coding:utf-8-*-
def topic_render(topic,wordNumbers,vocabArray):
    terms = topic[0]
    termWeights = topic[1]
    result = []
    for i in range(wordNumbers):
        term = vocabArray[terms[i]]
        result.append((term,termWeights[i]))
    return result
def main():
	p = sys.argv[1]
	logFile = "data/" + p + "_cleaned.txt"
	sc = SparkContext("local", "simpleApp")
	sqlContext = SQLContext(sc)
	data = sc.textFile(logFile).zipWithIndex().map(lambda (words,idd): Row(idd= idd, words = words.split(" "))).cache()
	docDF = sqlContext.createDataFrame(data)
	Vector = CountVectorizer(inputCol="words", outputCol="vectors")
	model = Vector.fit(docDF)
	result = model.transform(docDF)
	corpus_size = result.count()
	
	corpus = result.select("idd", "vectors").map(lambda (x,y): [x,y]).cache()
	
	# Cluster the documents into three topics using LDA
	ldaModel = LDA.train(corpus, k=3,maxIterations=100,optimizer='online')
	topics = ldaModel.topicsMatrix()
	wordNumbers = 10
	topicIndices = sc.parallelize(ldaModel.describeTopics(maxTermsPerTopic = wordNumbers))
	vocabArray = model.vocabulary
	topics_final = topicIndices.map(lambda topic: topic_render(topic,wordNumbers,vocabArray)).collect()

	path = "data/" + p + "_results.txt"
	json = open(path, 'wb')
	json.close()

	for topic in topics_final:
		for term in topic:
			line = term + " "

			try:
				string_for_output = line.encode('utf8', 'replace')
				if string_for_output != " ":
					os.system("python3 basic/codes/p3p.py " +  string_for_output + "  >> " + path)
			except: pass

		os.system("python3 basic/codes/p3p.py " +  "delmch" + "  >> " + path)

if __name__ == "__main__":
	main()
