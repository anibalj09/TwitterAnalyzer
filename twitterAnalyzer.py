#import json
import os
import time

class tweetObject:
    userName = ""
    hourPosted = 0
    numFollowers = 0
    numRetweet = 0
    theTweet = ""
     
    def __init__(self, uName, hPost, aTweet, numFol, numRet):
        self.userName = uName
        self.hourPosted = hPost
        self.theTweet = aTweet
        self.numFollowers = numFol
        self.numRetweet = numRet 

class tweetAnalyze:
    
    usersVector = []
    uniqueUsers = []
    userTotalCount = []
    userFollowerCount = []
    userMaxRetweetCount = []
    
    def __init__(self):
        pass

    def initVector(self, fileName):
        aPlace = 0
        
        userName = ""
        hourPosted = 0
        tweetItself = ""
        numFollowers = 0
        numRetweet = 0
        aPlace = 0
        endPlace = 0
        tweetPlace = 0
        
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
                
                tweetPlace = aLine.find(']')
                tweetPlace += 3
                
                while True:
                    if aLine[aPlace] == ' ':
                        break
                    else:
                        aPlace = aPlace - 1
                endPlace = aPlace - 1
                
                tweetItself = aLine[tweetPlace:endPlace]
                #print "This is the tweet: " + tweetItself
                        
                aPlace += 1
                numFollowers = aLine[aPlace:tempPlace]
                print "This is the number of followers: " + numFollowers
                aTweetObject = tweetObject(userName, hourPosted, tweetItself, numFollowers, numRetweet)
                break
                self.usersVector.append(aTweetObject)
    
    def getBigPoster(self, numToFind):
        self.uniqueUsers = []
        self.userTotalCount = []
        sortedListU = []
        sortedListC = []
        
        for index, item in enumerate(self.usersVector):
            print "This is the current user name to check: " + item.userName
            numTimes = self.uniqueUsers.count(item.userName)
            if  numTimes == 0:
                print "Inserting new user: " + item.userName
                self.uniqueUsers.append(item.userName)
                self.userTotalCount.append(1)
            elif numTimes > 0:
                itemIndex = self.uniqueUsers.index(item.userName)
                print "Already in array."
                self.userTotalCount[itemIndex] += 1
                
        #for index, item in enumerate(userCount):
            #if index == 0:
                #sortedListU.append(uniqueUsers[0])
                #sortedListC.append(userCount[0])
            #elif 
        
        #Sorting algorithm taken from: https://stackoverflow.com/a/20257603
        for i in range(len(self.userTotalCount)):
            for j in range(len(self.userTotalCount) - 1):
                if self.userTotalCount[j] > self.userTotalCount[j+1]:
                    self.userTotalCount[j], self.userTotalCount[j + 1] = self.userTotalCount[j + 1], self.userTotalCount[j]
                    self.uniqueUsers[j], self.uniqueUsers[j + 1] = self.uniqueUsers[j + 1], self.uniqueUsers[j]
        
        aFile = open("BigPosters.txt", 'w')
        for index, item in enumerate(self.uniqueUsers):
            aLine = str(index+1) + ". " + str(item) + " #" + str(self.userTotalCount[index]) + '\n'
            aFile.write(aLine)
            if (index + 1) == numToFind:
                break
        aFile.close()
        
    def getBigFollower(self, numToFind):
        for item in self.usersVector:
            pass

def main():
    
    aFileName = raw_input("Enter the name of the file to analyze: ")
    fileExists = False
    if aFileName != None or aFileName != "":
        fileExists = os.path.isfile(aFileName)
    else:
        print "ERROR. INPUT WAS EMPTY."
        return -1
    if fileExists:
        aNumber = 0
        aNumToFind = raw_input("How many should we find? -> ")
        print aNumToFind
        if aNumToFind != None:
            try:
                aNumber = int(aNumToFind)
            except ValueError:
                print "This is not a number, or it's not an integer."
                return -1
            
            if aNumToFind > 0:
                anObject = tweetAnalyze()
                anObject.initVector(aFileName)
                #anObject.getBigPoster(aNumber)
                #anObject.getBigFollower(aNumber)
            else:
                print "It has to be bigger than 0."
                return -1                
        else:
            print "You left it empty."
            return -1
    else:
        print "File didn't exists. Try again."
        return -1

if __name__ == "__main__":
    main()

