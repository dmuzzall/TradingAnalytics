import sys
import numpy as np

def CountOutrights(pos):
    return sum(pos)

def CountSpreads(pos):
    if CountOutrights(pos) != 0:
        raise ValueError
    pos2 = pos.copy()
    sCount = 0
    while(len(pos2) > 1):
        sCount += pos2[0]
        pos2[1] += pos2[0]
        pos2.pop(0)
    return sCount

def CountSum(obj):
    return np.sum(np.abs(obj))

def RemoveOutright_LtoR(pos, nOut):
    trade = [0] * len(pos)
    print(trade)
    if nOut > 0:
        for p in range(len(pos)):
            if pos[p] > 0:
                trade[p] = min(pos[p], nOut)
                return trade
    elif nOut < 0:
        for p in range(len(pos)):
            if pos[p] < 0:
                trade[p] = max(pos[p], nOut)
                return trade
    else:
        return trade

def RemoveAllOutrights_LtoR(pos, tradeList):
    pos2 = pos.copy()
    while CountOutrights(pos2) != 0:
        nOut = CountOutrights(pos2)
        trade = RemoveOutright_LtoR(pos2, nOut)
        pos2 = np.subtract(pos2, trade).tolist()
        tradeList.append(trade)
    return [pos2, tradeList]

def RemoveAllOutrights_RtoL(pos, tradeList):
    pos2 = pos.copy()[::-1]
    tradeList2 = [trade[::-1] for trade in tradeList]
    [pos2, tradeList2] = RemoveAllOutrights_LtoR(pos2, tradeList2)
    return [pos2[::-1], [trade[::-1] for trade in tradeList2]]

def RemoveSpread_LtoR(pos, nSpr):
    trade = [0] * len(pos)
    if nSpr > 0:
        for p in range(len(pos)-1):
            if pos[p] > 0:
                trade[p] = min(pos[p], nSpr)
                trade[p+1] = -trade[p]
                return trade
    elif nSpr < 0:
        for p in range(len(pos)-1):
            if pos[p] < 0:
                trade[p] = max(pos[p], nSpr)
                trade[p + 1] = -trade[p]
                return trade
    else:
        return trade

def RemoveAllSpreads_LtoR(pos, tradeList):
    pos2 = pos.copy()
    while CountSpreads(pos2) != 0:
        nSpr = CountSpreads(pos2)
        trade = RemoveSpread_LtoR(pos2, nSpr)
        pos2 = np.subtract(pos2, trade).tolist()
        tradeList.append(trade)
    return [pos2, tradeList]

def RemoveAllSpreads_RtoL(pos, tradeList):
    pos2 = pos.copy()[::-1]
    tradeList2 = [trade[::-1] for trade in tradeList]
    [pos2, tradeList2] = RemoveAllSpreads_LtoR(pos2, tradeList2)
    return [pos2[::-1], [trade[::-1] for trade in tradeList2]]

def RemoveButterfly_LtoR(pos):
    trade = [0] * len(pos)
    for p in range(len(pos)-2):
        if pos[p] == 0: continue
        trade[p] = pos[p];
        trade[p+1] = pos[p] * (-2)
        trade[p+2] = pos[p]
        return trade
    return trade

def RemoveAllButterflies_LtoR(pos, tradeList):
    pos2 = pos.copy()
    while CountSum(pos2) != 0:
        trade = RemoveButterfly_LtoR(pos2)
        pos2 = np.subtract(pos2, trade).tolist()
        tradeList.append(trade)
    return [pos2, tradeList]

def RemoveAllButterflies_RtoL(pos, tradeList):
    pos2 = pos.copy()[::-1]
    tradeList2 = [trade[::-1] for trade in tradeList]
    [pos2, tradeList2] = RemoveAllButterflies_LtoR(pos2, tradeList2)
    return [pos2[::-1], [trade[::-1] for trade in tradeList2]]

def ParsePosition_LtoR(pos):
    pos2 = pos.copy()
    tradeList = []
    [pos2, tradeList] = RemoveAllOutrights_LtoR(pos2, tradeList)
    [pos2, tradeList] = RemoveAllSpreads_LtoR(pos2, tradeList)
    [pos2, tradeList] = RemoveAllButterflies_LtoR(pos2, tradeList)
    if np.sum(tradeList, axis=0).tolist() != pos:
        raise ValueError
    return tradeList

def ParsePosition_RtoL(pos):
    pos2 = pos.copy()
    tradeList = []
    [pos2, tradeList] = RemoveAllOutrights_RtoL(pos2, tradeList)
    [pos2, tradeList] = RemoveAllSpreads_RtoL(pos2, tradeList)
    [pos2, tradeList] = RemoveAllButterflies_RtoL(pos2, tradeList)
    if np.sum(tradeList, axis=0).tolist() != pos:
        raise ValueError
    return tradeList



pos = [1, -2, 1, -3, 2]
print("Initial: ", pos)

try:
    tradeList1 = ParsePosition_LtoR(pos)
    print("TradeList LtoR: ", tradeList1)
    n1 = CountSum(tradeList1)
    print("Count LtoR: ", n1)

    tradeList2 = ParsePosition_RtoL(pos)
    print("TradeList RtoL: ", tradeList2)
    n2 = CountSum(tradeList2)
    print("Count RtoL: ", n2)



except ValueError:
    print("ERROR ValueError")

