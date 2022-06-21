import sys
import numpy as np

class PosParsing:

    def CountOutrights(self, pos):
        return sum(pos)

    def CountSpreads(self, pos):
        if self.CountOutrights(pos) != 0:
            raise ValueError
        pos2 = pos.copy()
        sCount = 0
        while(len(pos2) > 1):
            sCount += pos2[0]
            pos2[1] += pos2[0]
            pos2.pop(0)
        return sCount

    def CountSum(self, obj):
        return np.sum(np.abs(obj))

    def RemoveOutright_LtoR(self, pos, nOut):
        trade = [0] * len(pos)
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

    def RemoveAllOutrights_LtoR(self, pos, tradeList):
        pos2 = pos.copy()
        while self.CountOutrights(pos2) != 0:
            nOut = self.CountOutrights(pos2)
            trade = self.RemoveOutright_LtoR(pos2, nOut)
            pos2 = np.subtract(pos2, trade).tolist()
            tradeList.append(trade)
        return [pos2, tradeList]

    def RemoveAllOutrights_RtoL(self, pos, tradeList):
        pos2 = pos.copy()[::-1]
        tradeList2 = [trade[::-1] for trade in tradeList]
        [pos2, tradeList2] = self.RemoveAllOutrights_LtoR(pos2, tradeList2)
        return [pos2[::-1], [trade[::-1] for trade in tradeList2]]

    def RemoveSpread_LtoR(self, pos, nSpr):
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

    def RemoveAllSpreads_LtoR(self, pos, tradeList):
        pos2 = pos.copy()
        while self.CountSpreads(pos2) != 0:
            nSpr = self.CountSpreads(pos2)
            trade = self.RemoveSpread_LtoR(pos2, nSpr)
            pos2 = np.subtract(pos2, trade).tolist()
            tradeList.append(trade)
        return [pos2, tradeList]

    def RemoveAllSpreads_RtoL(self, pos, tradeList):
        pos2 = pos.copy()[::-1]
        tradeList2 = [trade[::-1] for trade in tradeList]
        [pos2, tradeList2] = self.RemoveAllSpreads_LtoR(pos2, tradeList2)
        return [pos2[::-1], [trade[::-1] for trade in tradeList2]]

    def RemoveButterfly_LtoR(self, pos):
        trade = [0] * len(pos)
        for p in range(len(pos)-2):
            if pos[p] == 0: continue
            trade[p] = pos[p];
            trade[p+1] = pos[p] * (-2)
            trade[p+2] = pos[p]
            return trade
        return trade

    def RemoveAllButterflies_LtoR(self, pos, tradeList):
        pos2 = pos.copy()
        while self.CountSum(pos2) != 0:
            trade = self.RemoveButterfly_LtoR(pos2)
            pos2 = np.subtract(pos2, trade).tolist()
            tradeList.append(trade)
        return [pos2, tradeList]

    def RemoveAllButterflies_RtoL(self, pos, tradeList):
        pos2 = pos.copy()[::-1]
        tradeList2 = [trade[::-1] for trade in tradeList]
        [pos2, tradeList2] = self.RemoveAllButterflies_LtoR(pos2, tradeList2)
        return [pos2[::-1], [trade[::-1] for trade in tradeList2]]

    def ParsePosition_LtoR(self, pos):
        pos2 = pos.copy()
        tradeList = []
        [pos2, tradeList] = self.RemoveAllOutrights_LtoR(pos2, tradeList)
        [pos2, tradeList] = self.RemoveAllSpreads_LtoR(pos2, tradeList)
        [pos2, tradeList] = self.RemoveAllButterflies_LtoR(pos2, tradeList)
        if np.sum(tradeList, axis=0).tolist() != pos:
            raise ValueError
        return tradeList

    def ParsePosition_RtoL(self, pos):
        pos2 = pos.copy()
        tradeList = []
        [pos2, tradeList] = self.RemoveAllOutrights_RtoL(pos2, tradeList)
        [pos2, tradeList] = self.RemoveAllSpreads_RtoL(pos2, tradeList)
        [pos2, tradeList] = self.RemoveAllButterflies_RtoL(pos2, tradeList)
        if np.sum(tradeList, axis=0).tolist() != pos:
            raise ValueError
        return tradeList

    def ParsePosition(self, pos):
        try:
            tradeList1 = self.ParsePosition_LtoR(pos)
            n1 = self.CountSum(tradeList1)
            tradeList2 = self.ParsePosition_RtoL(pos)
            n2 = self.CountSum(tradeList2)

            if n2 < n1:
                return tradeList2
            else:
                return tradeList1

        except ValueError:
            print("ERROR ValueError")
            return []



# pos = [1, -2, 1, -3, 2]
# print("Initial: ", pos)
#
# posParsing = PosParsing()
# tradeList = posParsing.ParsePosition(pos)
# print("TradeList: ", tradeList)
