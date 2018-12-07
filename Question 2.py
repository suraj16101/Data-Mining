import numpy as np
import random
from scipy.spatial import distance

def CentroidCal(i):
    a = np.mean(i, axis=0)
    return a


def Distance(D1,D2):
    dist =distance.euclidean(D1,D2)
    #print ("Distance"+str(dist)+"D1"+str(D1)+"D2"+str(D2))
    return dist


def Representative(Array):
    temp=[]
    for i in Array:
        a=CentroidCal(i)
        temp.append(a)
    return temp




def Clustering(k,DataValue,d):
    Seed=[]
    Seed=[[1.0],[2.0],[3.0]]
    # Seed=[[1.0,2.0],[11.0,23.0],[28.0,32.0]]
    if(len(Seed)==0):
        temp = DataValue
        i = k
        while(i!=0):
            val = random.choice(temp)
            if(k<= len(DataValue) and val not in Seed):
                Seed.append(val)
                i+=-1
            if(k>len(DataValue)):
                print("Number of Clusters > Number of Points")
                main()
    print("initial",Seed)


    while(1):
        Cluster=[[] for i in Seed]
        for m in range(0, d):
            flag = -1
            index=0
            for n in range(0,k):
                min = Distance(DataValue[m], Seed[n])
                if(flag==-1):
                    flag = min

                if(flag>min):
                    flag = min
                    index = n
            Cluster[index].append(DataValue[m])
        print("cluster",Cluster)
        Seednew = Representative(Cluster)
        print("Seedafter",Seednew)

        if(np.array_equal(Seed,Seednew)):
            break
        else:
            Seed=Seednew

    print("Done")
    print("Cluster :- ",*Cluster,sep="\n")




def main():
    # k=int(input("Value of K - "))
    # d=int(input("No. of DataPoints - "))
    # DataValue=[]
    # for i in range(0,d):
    #     points=input("Point - ")
    #     DataValue.append(points.split(","))
    #
    # DataValue=[list(map(float, x)) for x in DataValue]

    #Reading From a File Testcase.txt

    k=int(input("Value of K - "))
    lines = [line.rstrip('\n').split(',') for line in open('Testcase.txt')]
    DataValue = [list(map(float, x)) for x in lines]

    Clustering(k,DataValue,len(DataValue))


main()