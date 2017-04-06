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


def test():

    board = ConnectFourBoard(6, 7)

    assert board.getBoard() == [[EMPTY] * 6] * 7

    print "Success"


def main():

    pass


if __name__ == "__main__":
    test()
    #main()
