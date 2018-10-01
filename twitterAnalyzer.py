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
        aPlace = 0
        endPlace = 0
        
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
                aTweetObject = tweetObject(userName, hourPosted, numFollowers, numRetweet)
                self.usersVector.append(aTweetObject)
    
    def getBigPoster(self, numToFind):
        uniqueUsers = []
        userCount = []
        sortedListU = []
        sortedListC = []
        
        for index, item in enumerate(self.usersVector):
            print "This is the current user name to check: " + item.userName
            numTimes = uniqueUsers.count(item.userName)
            if  numTimes == 0:
                print "Inserting new user: " + item.userName
                uniqueUsers.append(item.userName)
                userCount.append(1)
            elif numTimes > 0:
                itemIndex = uniqueUsers.index(item.userName)
                print "Already in array."
                userCount[itemIndex] += 1
                
        #for index, item in enumerate(userCount):
            #if index == 0:
                #sortedListU.append(uniqueUsers[0])
                #sortedListC.append(userCount[0])
            #elif 
        
        #Sorting algorithm taken from: https://stackoverflow.com/a/20257603
        for i in range(len(userCount)):
            for j in range(len(userCount) - 1):
                if userCount[j] > userCount[j+1]:
                    userCount[j], userCount[j + 1] = userCount[j + 1], userCount[j]
                    uniqueUsers[j], uniqueUsers[j + 1] = uniqueUsers[j + 1], uniqueUsers[j]
        
        aFile = open("BigPosters.txt", 'w')
        for index, item in enumerate(uniqueUsers):
            aLine = str(index+1) + ". " + str(item) + " #" + str(userCount[index]) + '\n'
            aFile.write(aLine)
            if (index + 1) == numToFind:
                break
        aFile.close()

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
                anObject.getBigPoster(aNumber)
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

