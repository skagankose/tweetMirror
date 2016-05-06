
stopwords=set(["acaba","altmış","altı","ama","bana",
"bazı","belki","ben","benden","beni","benim","bir","biri","birkaç","birkez","birşey","birşeyi","biz","bizden","bizi","bizim","bu",
"buna","bunda","bundan","bunu","bunun","da","daha","dahi","de","defa","diye","doksan","dokuz",
"dört","elli","en","gibi","hem","hep","hepsi","her","hiç","iki","ile","ise","için","katrilyon","kez","ki","kim","kimden","kime","kimi","kırk",
"milyar","milyon","mu","mü","nasıl","ne","neden","nerde","nerede","nereye","niye","niçin","on","ona","ondan","onlar","onlardan","onları","onların",
"onu","otuz","sanki","sekiz","seksen","sen","senden","seni","senin","siz","sizden","sizi","sizin","trilyon","tüm","ve","veya","ya","yani","yedi",
"yetmiş","yirmi","yüz","çok","çünkü","üç","şey","şeyden","şeyi","şeyler","şu","şuna","şunda","şundan","şunu","in","ın","un","ün","var"])

import pipeline_caller
import re
import sys
caller = pipeline_caller.PipelineCaller()
NLPToken = "ym0ZWsgRYCcDmg3B6M9hO0ViWxF4SImn"

def clean(searchQuery):
    input_file_name = str(searchQuery)
    f = open('data/%s_tweets.csv' % input_file_name, 'r')
    output_file_name = str(searchQuery)
    o =open('data/%s_cleaned.txt' % output_file_name, 'w')
    resultString = str()
    rString=str()
    for line in f:
        line = line.lower()
        line = line.replace("i̇","i")
        line = clearSomething(line)
        line = " ".join(re.split('\W+',line))
        if len(line) != 0:
            resultString += line + "*"
    resultString = caller.call('pipelineNoisy', resultString, NLPToken)
    for i in resultString.split("\n"):
        k = i.split("\t")
        if k[3]=="Verb" or k[2]=="_":
            pass
        else:
            rString+=k[2]+" "
    for line in rString.split("*"):
        line = clearStopwords(line)
        if len(line)!=0:
            o.write(line+"\n")
    f.close()
    o.close()
    return(0)

def clearSomething(line):

    rStr = str()
    for element in line.split():
        if not element.startswith('http') and not element.startswith('@') and not element.startswith('#') and "rt" not in element:
            rStr += element + " "
    return rStr

def clearStopwords(line):
    rStr = str()
    for element in line.split():
        if element not in stopwords :
            rStr += element + " "
    return rStr

if __name__ == "__main__":

    sq = sys.argv[1]
    clean(sq)
