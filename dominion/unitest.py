import dominion as d
import random
    
def test_initializeGame():
    randomSeed = 111
    kingdomCards_Valid = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    kingdomCards= random.sample([d.Curse, d.Estate, d.Duchy, d.Province, d.Copper, d.Silver, d.Gold, d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Mine, d.Minion, d.Outpost, d.Remodel, d.Salvager, d.Sea_Hag, d.Smithy, d.Treasure_Map, d.Village],10)
    print "Testing Initialize Game with Bad set of Kingdom Cardsand Number of players"
    print kingdomCards
    players = random.randint(0,5)
    a = d.initializeGame(players, kingdomCards, randomSeed)
    assert(a == -1)
    print "Initilize Game() is invalid for kingdomCards selected and players: %d" %players
    print "Expected: " + "-1"
    print "Actual: %d " %a
    print "TEST PASS"
    if (a!= -1):
        print "TEST FAIL"
        print "Accepting bad input of kingdom cards for players %d" %players
    
    print "Testing Supply count of copper cards for all number of players and with valid kingdom cards"
    players = random.randint(2,4)
    b = d.initializeGame(players, kingdomCards_Valid, randomSeed)
    assert(b.supplyCount[d.Copper] == (60- 7* players))
    print "TEST PASS"
    print "Taking correct count of Copper cards: %d in supply for Players : %d" %(b.supplyCount[d.Copper],players)
    if (b.supplyCount[d.Copper] != (60- 7* players)):
        print "TEST FAIL"
        print "Taking wrong count of Copper cards: %d in supply for Players : %d" %(b.supplyCount[d.Copper],players)

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
        print "Invalid Input:deck empty"
    assert(b ==0)
    print "TEST PASS"
    print "After drawing"
    print "Deck"
    print a.deck
    print "Hand"
    print a.hand

def test_updateCoins():
    randSeed = 111
    numPlayers =random.randint(2,4) 
    maxBonus = random.randint(2,5)
    maxHandCount = random.randint(2,5)
    kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print "TESTING UpdateCoins()"
    a = d.initializeGame(numPlayers,kingdomCards, randSeed)
    assert(a !=-1)
    for i in range(numPlayers):
        a.hand[i] = []
    for player in range(numPlayers):
        for handCount in range(1,maxHandCount+1):
            a.hand[player].append(d.Copper)
            print a.hand[player]
            for bonus in range(maxBonus):
                b = d.updateCoins(player,a,bonus)
                assert(b ==0)
                print "TEST PASS"
                print "Return Value for player: %d, bonus %d and hand count : %d is %d" %(player,bonus, handCount, b)
                print "Expected value : 0"
                if (b != 0):
                    print "TEST FAIL"
                    print "Return Value for player: %d, bonus %d and hand count : %d is %d" %(player,bonus, handCount, b)
                    print "Expected value : 0"
                assert(a.coins == (handCount * 1 + bonus))
                print "TEST PASS"
                print "Testing with all copper coins for player : %d, bonus : %d, handCount : %d, Coin Value = %d" %(player,bonus,handCount,a.coins)
                print "Expected = %d" %(handCount *1 +bonus)
                if (a.coins != (handCount * 1 + bonus)):
                    print "TEST FAIL"
                    print "Testing with all copper coins for player : %d, bonus : %d, handCount : %d, Coin Value = %d" %(player,bonus,handCount,a.coins)
                    print "Expected = %d" %(handCount *1 +bonus)


def test_buyCard_gainCard():
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
    if(b ==0):
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

def test_getCost():
    print("Testing getCost()")
    card = d.Smithy
    print("Getting cost of card: %d" %card)
    r=d.getCost(card)
    assert(r==4)
    print ("Cost of card : %d is %d" %(card,r))
    
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
    if(b ==0):
        print "TEST PASS"
        print "After playing"
        print "hand"
        print a.hand[0]
        print "Card played by Player:0 is "
        print card

def test_scoreFor():
    kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print("Testing scoreFor()")
    r = d.initializeGame(2, kingdomCards,111)
    assert(r!=-1)
    print "Hand"
    print r.hand[0]
    print "Deck"
    print r.deck[0]
    print "Discard"
    print r.discard[0]
    x = d.scoreFor(0,r)
    assert(x!= -1)
    print ("Score for player : 0 is:")
    print x


def test_getWinners():
    kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print("Tetsing getWinners")
    p = d.initializeGame(2, kingdomCards,111)
    p.discard[0].append(d.Province)
    r = d.getWinners(p)
    assert(r!=-1)
    print("Player Won:")
    print r

def test_isGameOver():
    kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print("Tetsing isGameOver")
    r = d.initializeGame(2, kingdomCards,111)
    r.supplyCount[d.Province] = 0
    s = d.isGameOver(r)
    assert(s == 1)
    print ("Game Over: SUpply of province exhausted")
    print "Supply of province:"
    print r.supplyCount[d.Province]

    r = d.initializeGame(2, kingdomCards,111)
    r.supplyCount[d.Duchy] = 0
    r.supplyCount[d.Estate] = 0
    r.supplyCount[d.Village] = 0
    s = d.isGameOver(r)
    assert(s == 1)
    print ("Game Over:Supply of 3 piles is empty")
    print r.supplyCount[d.Duchy]
    print r.supplyCount[d.Estate]
    print r.supplyCount[d.Village]


def test_endTurn():
    kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cutpurse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print("Testing endTurn")
    r= d.initializeGame(2, kingdomCards,111)
    assert(r != -1)
    print ("Whose Turn:")
    print r.whoseTurn
    s = d.endTurn(r)
    assert (s == 0)
    print ("After endTurn:")
    print ("Whose Turn:")
    print r.whoseTurn

    
for i  in range(2):
    test_initializeGame()
    test_shuffle()
    test_drawCard()
    test_updateCoins()
    test_buyCard_gainCard()
    test_discardCard()
    test_getCost()
    test_playCard()
    test_scoreFor()
    test_getWinners()
    test_isGameOver()
    test_endTurn()
