#import json
import os
improt FileNotFoundError

class tweetObject:
	 userName = ""
     hourPosted = 0
     numFollowers = 0
     numRetweet = 0
     
    def __init__(self, uName, hPost, numFol, numRet):
        self.userName = uName
        self.hourPosted = hPost
        self.numFollowers = numFol
        self.numRetweet = numRet 

class tweetAnalyze:
    
    usersVector = []
    
    def __init__(self):
        pass

    def initVector(self, fileName):
        aLine = ""


def main():
    
    aFileName = raw_input("Enter the name of the file to analyze: ")
    fileExists = False
    if aFileName != None or aFileName != "":
        fileExists = os.path.isfile(aFileName)
    else:
        print "ERROR. INPUT WAS EMPTY."
        return -1
    
    if fileExists:
        anObject = tweetAnalyze()
        anObject.initVector(aFileName)
    else:
        print "File didn't exists. Try again."

if __name__ == "__main__":
    main()
