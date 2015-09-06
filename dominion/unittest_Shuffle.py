import random
import dominion as d
def test_shuffle():
    randSeed = 111
    numPlayers = 4
    kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print "TESTING Shuffle()"
    a = d.initializeGame(numPlayers,kingdomCards, randSeed)
    assert(a !=-1)
    print "Before Shuffle"
    print "Deck"
    print a.deck
    for turn in range(4):
        b = d.shuffle(turn,a)
    if (b == -1):
        print "Invalid Input:card not in hand OR SupplyEmpty"
    assert(b ==0)
    print "TEST PASS"
    print "After Shuffling"
    print "Deck"
    print a.deck
for i in range(10):
    test_shuffle()
