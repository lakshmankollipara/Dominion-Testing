import random
import dominion as d
def test_playCard():
    randSeed = 111
    card = random.randint(0,26)
    numPlayers = 4
    kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print "TESTING playCard()"
    a = d.initializeGame(numPlayers,kingdomCards, randSeed)
    assert(a !=-1)
    print "Before playing"
    print "hand of Player 0:"
    print a.hand[0]
    print "Card played by Player : 0 is "
    print card
    hpos = random.randint(0,4)
    b = d.playCard(hpos,0,0,0,a)
    if (b == -1):
            if card not in a.kingdomCards:
                print "Invalid Input:Card is Not KingdomCard"
            elif card not in a.hand[a.whoseTurn]:
                print "Invalid input, Card trying to play is not in hand"
    assert(b ==0)
    print "TEST PASS"
    print "After playing"
    print "hand"
    print a.hand[0]
    print "Card played by Player:0 is "
    print card

for i in range(10):
    test_playCard()
