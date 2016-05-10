from django.shortcuts import render
import basic.codes.tweetDumper as td
import os
import time
from models import Results

def searchPage(request):

	context = {}
	return render(request, 'searchPage.html', context)

def findTweets(request):

	if request.method == 'POST':
		searchQuery = request.POST.get('search')

		try:
			tmpModel = Results.objects.get(username=searchQuery)

		except:

			location = 'data/' + searchQuery + '_results.txt'
			results = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

			try:

				topic = 0
				word = 0
				with open(location, 'r') as F:

					for line in F:

						if word < 9:
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

						# RETRIEVING TWEETS
						td.get_all_tweets(str(searchQuery))

				try:

					location = 'data/' + searchQuery + '_cleaned.txt'
					with open(location, 'r') as F:
						pass

				except:

					# CLEANING DATA WITH TURKISH NLP
					nlpPath = 'basic/codes/NLPTurkish.py'
					os.system("python3 " +  " " + nlpPath + " " + searchQuery)

				# RUNNING SPARK
				sparkPath = '/Users/k/Spark/bin/spark-submit'
				scriptPath = 'basic/codes/simpleApp.py'
				os.system(sparkPath + " --master local[4] " + scriptPath + " " + searchQuery)

				print("Last seconds...")
				time.sleep(2)

				location = 'data/' + searchQuery + '_results.txt'
				results = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]


				try:
					topic = 0
					word = 0
					with open(location, 'r') as fp:

						for line in fp:

							if word < 9:
								results[topic][word] = line.strip("\n")
								word += 1
							else:
								word = 0
								topic += 1
				except:
					context = {}
					return render(request, 'searchPage.html', context)


			# SAVING FINDINGS TO DATABASE
			tmpModel = Results(username=searchQuery)
			tmpModel.t1w1 = results[0][0]
			tmpModel.t1w2 = results[0][1]
			tmpModel.t1w3 = results[0][2]
			tmpModel.t1w4 = results[0][3]
			tmpModel.t1w5 = results[0][4]
			tmpModel.t1w6 = results[0][5]
			tmpModel.t1w7 = results[0][6]
			tmpModel.t2w1 = results[1][0]
			tmpModel.t2w2 = results[1][1]
			tmpModel.t2w3 = results[1][2]
			tmpModel.t2w4 = results[1][3]
			tmpModel.t2w5 = results[1][4]
			tmpModel.t2w6 = results[1][5]
			tmpModel.t2w7 = results[1][6]
			tmpModel.t3w1 = results[2][0]
			tmpModel.t3w2 = results[2][1]
			tmpModel.t3w3 = results[2][2]
			tmpModel.t3w4 = results[2][3]
			tmpModel.t3w5 = results[2][4]
			tmpModel.t3w6 = results[2][5]
			tmpModel.t3w7 = results[2][6]
			tmpModel.save()


		# RETURNING REQUESTED PAGE 
		context = {"searchQuery":searchQuery, "tmpModel":tmpModel}
		return render(request, 'findTweets.html', context)
