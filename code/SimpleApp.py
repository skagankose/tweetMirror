from pyspark import SparkContext
import sys

def main():
    p = sys.argv[1]
    logFile = "data/" + p + "_tweets.csv"
    sc = SparkContext("local", "simpleApp")
    logData = sc.textFile(logFile).cache()

    # Start Here
    logData = logData.map(lambda x: (x,"Spark has been used!"))
    result = logData.collect()

    # No need
    for element in result:

        # Check whether all chracters are ASCII
        try:
            print element[0] + " - " + element[1]
        except:
            pass

if __name__ == "__main__":
    main()
