# -*- coding: cp936 -*-
"""
Apriori算法
Ben
2015.09.28
"""
# coding:utf-8
from numpy import *


def loadData():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5], [2, 4, 6, 8], [1, 3]]


def createC1(dataSet):  # 生成C1
    c1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    c1.sort()
    return list(map(frozenset, c1))


def scanD(D, Ck, minSupport):  # 计算支持度
    # 计算集合计数
    ssCnt = {}
    for transaction in D:
        for candidate in Ck:
            if candidate.issubset(transaction):  # 判断candidate中
                if candidate not in ssCnt:
                    ssCnt[candidate] = 1
                else:
                    ssCnt[candidate] += 1
    # 计算支持度
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData


# test
dataSet = loadData()
c1 = createC1(dataSet)
D = list(map(set, dataSet))
L1, supportData = scanD(D, c1, 0.5)
print(L1)
print(supportData)