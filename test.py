import Apriori.py

#test
dataSet = loadData()
c1 = createC1(dataSet)
D = map(set,dataSet)
L1,supportData = scanD(D,c1,0.5)
print L1
print supportData