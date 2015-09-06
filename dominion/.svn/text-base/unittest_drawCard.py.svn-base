import random
import dominion as d
def test_drawCard():
    randSeed = 111
    numPlayers = 4
    kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print "TESTING drawCard()"
    a = d.initializeGame(numPlayers,kingdomCards, randSeed)
    assert(a !=-1)
    print "Before drawing"
    print "Deck"
    print a.deck
    print "Hand"
    print a.hand
    for turn in range(4):
        b = d.drawCard(turn,a)
    if (b == -1):
        print "Invalid Input:deckempty"
    assert(b ==0)
    print "TEST PASS"
    print "After drawing"
    print "Deck"
    print a.deck
    print "Hand"
    print a.hand
for i in range(10):
    test_drawCard()
