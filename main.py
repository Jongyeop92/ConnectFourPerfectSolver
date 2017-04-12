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


import pickle
import copy


EMPTY  = '_'
FIRST  = 'X'
SECOND = 'O'


class Position:

    def __init__(self):
        self.WIDTH = 7
        self.HEIGHT = 6
        self.WIN_COUNT = 4

        self.moves = 0
        self.directionPairList = [[(-1, 0), ( 1,  0)],
                                  [(-1, 1), ( 1, -1)],
                                  [( 0, 1), ( 0, -1)],
                                  [( 1, 1), (-1, -1)]]

        self.board = [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]

    def canPlay(self, col):
        return self.board[0][col] == EMPTY

    def play(self, col, color):
        row = self.HEIGHT - 1
        while self.board[row][col] != EMPTY:
            row -= 1

        self.board[row][col] = color
        self.moves += 1

        return row

    def isWinningMove(self, col, color):
        row = 0

        while row < self.HEIGHT and self.board[row][col] == EMPTY:
            row += 1
        row -= 1

        y, x = row, col
        
        for directionPair in self.directionPairList:
            sameCount = 1
            for direction in directionPair:
                dy, dx = direction
                nowY, nowX = y, x

                while self.isInBoard(nowY + dy, nowX + dx):
                    nowY += dy
                    nowX += dx

                    if self.board[nowY][nowX] == color:
                        sameCount += 1
                    else:
                        break

            if sameCount >= self.WIN_COUNT:
                return True

        return False

    def isInBoard(self, y, x):
        return 0 <= y and y < self.HEIGHT and 0 <= x and x < self.WIDTH

    def key(self):
        k = ''.join(''.join(row) for row in self.board)

        compressedKey = ''

        ch = k[0]
        count = 1
        for i in range(1, len(k)):
            if ch == k[i]:
                count += 1
            else:
                if count > 1 or ch == EMPTY:
                    compressedKey += str(count) + ch
                else:
                    compressedKey += ch

                ch = k[i]
                count = 1

        compressedKey += str(count) + ch

        return compressedKey.replace(EMPTY, '')

def saveObject(obj, fileName):
    with open(fileName, "wb") as f:
        pickle.dump(obj, f)


def loadObject(fileName):
    with open(fileName, "rb") as f:
        return pickle.load(f)


def negamax(p, nowColor, nextColor):

    key = p.key()

    if tt.get(key) != None and len(tt[key]) == p.WIDTH:
        return tt[key]

    if p.moves == p.WIDTH * p.HEIGHT:
        print "draw"
        return [(0, None)]

    for col in range(p.WIDTH):
        if p.canPlay(col) and p.isWinningMove(col, nowColor):
            print nowColor, "win"
            return [((p.WIDTH * p.HEIGHT + 1 - p.moves) / 2, col)]

    bestScore = -p.WIDTH * p.HEIGHT
    bestMove = None

    tt[key] = []

    for col in range(p.WIDTH):
        if p.canPlay(col):
            copyP = copy.deepcopy(p)
            copyP.play(col, nowColor)

            score, move = max(negamax(copyP, nextColor, nowColor))

            tt[key].append((-score, col))

            if -score > bestScore:
                bestScore = -score
                bestMove = move
        else:
            tt[key].append(None)

    return tt[key]


ttFileName = "connect_four_tt"
try:
    tt = loadObject(ttFileName)
except:
    tt = {}


def test():

    p = Position()

    assert p.board == [[EMPTY] * 7] * 6

    assert p.canPlay(0) == True
    assert p.canPlay(6) == True

    p.play(0, FIRST)
    p.play(0, FIRST)
    p.play(0, FIRST)
    assert p.board == [[EMPTY] * 7] * 3 + \
                      [[FIRST] + [EMPTY] * 6] + \
                      [[FIRST] + [EMPTY] * 6] + \
                      [[FIRST] + [EMPTY] * 6]
    
    assert p.isWinningMove(0, FIRST) == True
    assert p.isWinningMove(0, SECOND) == False

    p2 = Position()

    print negamax(p2, FIRST, SECOND)

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
        saveObject(tt, ttFileName)
