from django.shortcuts import render
import basic.codes.tweetDumper as td
import os


def searchPage(request):

	context = {}
	return render(request, 'searchPage.html', context)

def findTweets(request):

	if request.method == 'POST':
		searchQuery = request.POST.get('search')

		location = 'data/' + searchQuery + '_results.txt'
		results = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

		try:

			topic = 0
			word = 0
			with open(location, 'r') as F:

				for line in F:

					if word < 7:
						# print topic, word
						results[topic][word] = line.strip("\n")
						word += 1
					else:
						word = 0
						topic += 1

		except:

			try:
					ts = 'data/' + searchQuery + '_tweets.csv'
					with open(ts, 'r') as F:
						pass

			except:

					# Retrieve Tweets
					td.get_all_tweets(str(searchQuery))

			# Run Turkish NLP
			nlpPath = 'basic/codes/NLPTurkish.py'
			os.system("python3 " +  " " + nlpPath + " " + searchQuery)

			# Run Spark
			sparkPath = '/Users/k/Spark/bin/spark-submit'
			scriptPath = 'basic/codes/simpleApp.py'
			os.system(sparkPath + " --master local[4] " + scriptPath + " " + searchQuery)

			# Read Results
			topic = 0
			word = 0
			with open(location, 'r') as F:

				for line in F:

					if word < 7:
						# print topic, word
						results[topic][word] = line.strip("\n")
						word += 1
					else:
						word = 0
						topic += 1


		context = {"searchQuery":searchQuery, "results": results}
		return render(request, 'findTweets.html', context)
