import random

global sample
sample=[]

def getNextStream(n,N):
    stream=[]
    for i in range (n):
        value =random.choice(N)
        N.remove(value)
        stream.append(value)

    return stream



def updateSample( streamItem, itemNumber):


    if(itemNumber<=s):
        if (len(sample) == s):
            value = random.choice(sample)
            sample.remove(value)
        sample.append(streamItem)
        count[itemNumber-1] = count[itemNumber-1] + 1

    else:
        value=random.uniform(0, 1)
        if(s/itemNumber>=value):
            if (len(sample) == s):
                value = random.choice(sample)
                sample.remove(value)
            sample.append(streamItem)
            count[itemNumber-1] = count[itemNumber-1] + 1




def main():
    No_tweets = [100, 500, 1000, 10000]                 # Number of tweets 100,500,1000,10000
    for tweet in No_tweets:
        N = list(range(1, tweet+1))                     # Dummy Tweet generation
        stream = getNextStream(20, N)                   # Data stream size 20
        global count
        count = [0]*len(stream)
        global s
        s = 5                                           # Sample of size =5
        for i in range(100):
            samplevalue = random.choice(stream)
            updateSample(samplevalue, stream.index(samplevalue)+1)
        print("N =",tweet)
        print(stream)
        for pr in range (len(count)):
            print("A"+str(pr+1), "=",count[pr], end = "\t")
        print("\n")




main()
