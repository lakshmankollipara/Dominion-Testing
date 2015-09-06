import random
import dominion as d
def test_gainCard():
    randSeed = 111
    card = random.randint(0,26)
    numPlayers = 4
    turn = random.randint(0,3)
    kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print "TESTING gainCard()"
    a = d.initializeGame(numPlayers,kingdomCards, randSeed)
    assert(a !=-1)
    print "Before gaining"
    print "Deck"
    print a.deck
    print "Card Gaining by Player : %d is " %turn
    print card
    print "Supply Count of Card:"
    print a.supplyCount[card]
    b = d.gainCard(card,a,1,turn)
    if (b == -1):
        print "Invalid Input:Supply Empty"
    assert(b ==0)
    print "TEST PASS"
    print "After gaining"
    print "Deck"
    print a.deck
    print "Card gained by Player %d is "%turn
    print card
    print "Supply Count of Card:"
    print a.supplyCount[card]
for i in range(10):
    test_gainCard()
