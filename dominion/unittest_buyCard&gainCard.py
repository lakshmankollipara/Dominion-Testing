import random
import dominion as d
def test_buyCard():
    randSeed = 111
    numPlayers =random.randint(2,4) 
    maxBonus = random.randint(2,5)
    maxHandCount = random.randint(2,5)
    kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    card = random.randint(d.Curse,d.Village)
    print "TESTING UpdateCoins()"
    a = d.initializeGame(numPlayers,kingdomCards, randSeed)
    assert(a !=-1)
    a.whoseTurn = random.randint(0,numPlayers-1)
    print "Before Buying"
    print "Card want to Buy:"
    print card
    print "Cost of Card"
    x = d.getCost(card)
    print x
    print "Coins Available:"
    print a.coins
    print "numBuys available"
    print a.numBuys
    print "Whose Turn:"
    print a.whoseTurn
    print "Discard"
    print a.discard
    print "Supply of Card"
    print a.supplyCount[card]
    b = d.buyCard(card,a)
    if (b == -1):
        print "Invalid Input:No numBuys OR No enough Coins OR SupplyEmpty"
    assert(b ==0)
    print "BuyCard() is successfull for player : %d brought: %d" %(a.whoseTurn,card)
    print "After Buying"
    print "Card Bought:"
    print card
    print "Coins Available:"
    print a.coins
    print "numBuys available"
    print a.numBuys
    print "Whose Turn:"
    print a.whoseTurn
    print "Discard"
    print a.discard
    print "Supply of Card"
    print a.supplyCount[card]

for i in range(10):
    test_buyCard()
