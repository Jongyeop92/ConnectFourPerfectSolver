# -*- coding: utf8 -*-

# Perfect Solver 만들기
#
# - minmax
# - alpha-beta
# - search order
# - exploration order
# - (option) bitboard
# - transposition table
# - iterative deepening

from ConnectFourBoard import *

import pickle

def saveObject(obj, fileName):
    with open(fileName, "wb") as f:
        pickle.dump(obj, f)

def loadObject(fileName):
    with open(fileName, "rb") as f:
        return pickle.load(f)
    
def makeTranspositionTable(state, player):

    possiblePositionList = state.getPossiblePositionList(player)

    for position in possiblePositionList:
        pass

def getPositionData(state, player):

    key = state.getCompressedBoardStr()

    if key not in tt:
        makeTranspositionTable(state, player)
        return False
    
    return tt[key]

def setState(state, positionList):

    nowPlayer, nextPlayer = state.FIRST, state.SECOND

    for position in positionList:
        state.setMarker(nowPlayer, position)

        nowPlayer, nextPlayer = nextPlayer, nowPlayer


ttFileName = "tt"
try:
    tt = loadObject(ttFileName)
except:
    tt = {}


def test():

    state = ConnectFourBoard(8, 8)

    #assert getPositionData(state, state.FIRST) == False

    #tt[state.getCompressedBoardStr()] = []

    assert getPositionData(state, state.FIRST) == False
    

    print "Success"


def main():

    pass


if __name__ == "__main__":
    try:
        test()
        #main()
    except Exception as e:
        print e
        print "saving tt..."
    finally:
        pass
        #saveObject(tt, ttFileName)
