# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 2015

@author: huynhant
"""

import Dominion
import random
from collections import defaultdict
import testUtility

# Get player names
player_names = testUtility.GetPlayerNames()

# number of curses and victory cards
nV = testUtility.GetNV(player_names)
nC = -10 + 10 * len(player_names)

# get box
box = testUtility.GetBoxes(nV)

# get supply order
supply_order = testUtility.GetSupplyOrder()

# Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)

# game will only have one card from box to be in the supply
random10 = boxlist[:1]

supply = defaultdict(list, [(k, box[k]) for k in random10])

# Get supply
supply = testUtility.SupplyAlwaysHas(supply, player_names, nV, nC)

# initialize the trash
trash = []

# Contruct the Player objects
players = testUtility.ConstructPlayers(player_names)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)