#import json
import os
import time

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
        aPlace = 0
        
        userName = ""
        hourPosted = 0
        numFollowers = 0
        numRetweet = 0
        
        
        with open(fileName) as aFile:
            for aLine in aFile:
                aPlace = aLine.find('[')
                userName = aLine[:(aPlace-1)]
                print "This is the username found: " + userName
                aPlace +=1
                aPlace +=12
                hourPosted = aLine[aPlace:(aPlace + 2)]
                print "This is the hour posted: " + hourPosted
                aPlace = len(aLine)
                aPlace = aPlace - 1
                while True:
                    if aLine[aPlace] == ' ':
                        break
                    else:
                        aPlace = aPlace - 1
                        
                aPlace += 1
                endPlace = aLine.find('\n')
                #endPlace = endPlace - 1
                numRetweet = aLine[aPlace:endPlace]
                print "This is the number of retweets: " + numRetweet
                tempPlace = aPlace - 1
                aPlace = aPlace - 2
                while True:
                    if aLine[aPlace] == ' ':
                        break
                    else:
                        aPlace = aPlace - 1
                        
                aPlace += 1
                numFollowers = aLine[aPlace:tempPlace]
                print "This is the number of followers: " + numFollowers
                break
        
        time.sleep(5)


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

