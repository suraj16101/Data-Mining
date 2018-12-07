import math
import numpy

def classifyNB(testPoint):
    LabelTest = []
    for i in testPoint:
        values = 0
        save = ""
        for k in tempflag:
            prob = 1 * totalprob[k]
            j=0
            while j< (len(i)):
                prob = prob * gaussian_distribution(i[j], Labelmean[k][j], Lablestd[k][j])
                j+=1
            if(values<prob):
                save = k
                values = prob

        LabelTest.append(save)

    return LabelTest


def filewrite(LabelTest):
    f = open("labels.txt", "w")
    for i in LabelTest:
        f.writelines(i + '\n')

def gaussian_distribution(x, mean, stdev):

    # Correcting the Error
    if(stdev==0):
        stdev=1

    exponent = math.exp(-(((x - mean) ** 2) / (2 * (stdev ** 2))))
    return (1 / (stdev * ((2 * math.pi) ** (1 / 2)))) * exponent


def StandardDV(val):
    return numpy.std(numpy.transpose(val), axis=1)


def mean(val):
    return numpy.mean(numpy.transpose(val), axis=1)


def trainNB(featureMatrix, labels):

    global Labledict
    global Labelmean
    global Lablestd
    Labledict = {}


    for i in range(len(labels)):
        if labels[i] not in Labledict:
            Labledict[labels[i]] = [featureMatrix[i]]
        else:
            Labledict[labels[i]].append(featureMatrix[i])

    Labelmean = {}
    Lablestd = {}
    for i in Labledict:
        Labelmean[i] = mean(Labledict[i])
        Lablestd[i] = StandardDV(Labledict[i])


def main():
    featureMatrix = []
    labels = []
    lines = [line.rstrip('\n').split(',') for line in open('train.txt')]

    for i in lines:
        labels.append(i[-1])
        featureMatrix.append(i)
        del i[-1]
    featureMatrix = [list(map(float, x)) for x in featureMatrix]


    global totalprob
    global tempflag
    totalprob = {}
    tempflag = set(labels)
    for i in tempflag:
        totalprob[i] = labels.count(i)/len(labels)

    x = numpy.array_split(featureMatrix, 10)
    y = numpy.array_split(labels, 10)

    fm =[]
    lb =[]
    sumval = 0
    for i in range(0, 10):
        for j in range(0, 10):
            if(i!=j):
                for k in range(0,len(x[j])):
                   fm.append(x[j][k])
                   lb.append(y[j][k])

        trainNB(fm, lb)
        temptest = classifyNB(x[i])
        temptest1 = y[i]
        count1 = 0
        for a in range (0,len(temptest1)):
            if(temptest[a] == temptest1[a]):
                count1 +=1
        sumval = sumval + (count1)/len(temptest1)


        fm =[]
        lb =[]


    trainNB(featureMatrix, labels)
    testfeatureMatrix = [line.rstrip('\n').split(',') for line in open('test.txt')]
    testfeatureMatrix = [list(map(float, x)) for x in testfeatureMatrix]
    FinalValToWrtie = classifyNB(testfeatureMatrix)
    filewrite(FinalValToWrtie)

    Accuracy = (sumval/10)*100
    print("Accuracy",Accuracy)


main()