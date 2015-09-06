import random
import dominion as d
def test_discardCard():
    randSeed = 111
    numPlayers =random.randint(2,4) 
    kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    card = d.Copper ##random.randint(d.Curse,d.Village)
    print "TESTING UpdateCoins()"
    a = d.initializeGame(numPlayers,kingdomCards, randSeed)
    assert(a !=-1)
    print "Before discard"
    print "Card to discard:"
    print card
    print "hand before discarding"
    print a.hand
    print "Coins available:"
    print a.coins
    b = d.discardCard(card,a.whoseTurn,a,0)
    c = d.updateCoins(a.whoseTurn,a,0)
    if (b == -1):
        print "Invalid Input:card not in hand OR SupplyEmpty"
    assert(b ==0)
    print "TEST PASS"
    print "discardCard() is successfull for player : %d discarded %d" %(a.whoseTurn,card)
    print "After Discarding"
    print "Card Discarded:"
    print card
    print "Hand after Discarding"
    print a.hand
    print "Coins Available:"
    print a.coins
for i in range(10):
    test_discardCard()
