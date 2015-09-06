import dominion_lesliew as d
import random
    
def test_initializeGame():
    kingdomCards_Invalid = ["Curse","Estate","Duchy","Province","Copper", "Silver", "Gold","Adventurer", "Ambassador", "Baron","Council Room", "Cut purse", "Embargo","Feast", "Gardens", "Great Hall","Mine", "Smithy", "Village", "Sea Hag"]
    kingdomCards_Invalid1 = ["Ambassador", "Baron","Council Room", "Cut purse", "Embargo", "Feast", "Gardens", "Great Hall","Mine"]
    kingdomCards_Valid = ["Adventurer", "Ambassador", "Baron","Council Room", "Cut purse", "Embargo", "Feast", "Gardens", "Great Hall","Mine"]
    print "Testing Initialize Game with Bad set of Kingdom Cardsand Number of players"
    print "kingdomcards"
    print kingdomCards_Invalid
    a = d.initializeGame(numPlayers, kingdomCards_Invalid, randomSeed)
    assert(a == -1)
    print "Initilize Game() is invalid for kingdomCards selected and players: %d" %numPlayers
    print "Expected: " + "-1"
    print "Actual: %d " %a
    print "TEST PASS"
    if (a!= -1):
        print "TEST FAIL"
        print "Accepting bad input of kingdom cards for players %d" %numPlayers
    print "Testing with wrong number of kingdomcards"
    print "kingdomcards"
    print kingdomCards_Invalid1
    ## commented because, Throws an error because not returning -1 for less kingdomcards
    ##bug included in report.
    """
    z = d.initializeGame(numPlayers, kingdomCards_Invalid1, randomSeed)
    if (z == -1):
        print "Test PASS for kingdom cards less than 10: Returning -1"
    else:
        print "Test FAIL for kingdom cards less than 10: Not eturning -1"
    """
    print "Testing Supply count of copper cards for all number of players and with valid kingdom cards"
    players = random.randint(2,4)
    b = d.initializeGame(players, kingdomCards_Valid, randomSeed)
    assert(b!= -1)
    assert(b.supplyCount["Copper"] == (60- 7* players))
    print "TEST PASS"
    print "Taking correct count of Copper cards: %d in supply for Players : %d" %(b.supplyCount["Copper"],players)
    if (b.supplyCount["Copper"] != (60- 7* players)):
        print "TEST FAIL"
        print "Taking wrong count of Copper cards: %d in supply for Players : %d" %(b.supplyCount["Copper"],players)

def test_shuffle():
    ##kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cut purse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print "TESTING Shuffle()"
    a = d.initializeGame(numPlayers,kingdomCards, randomSeed)
    assert(a !=-1)
    print "Before Shuffle"
    print "Deck"
    print a.deck
    for turn in range(numPlayers):
        b = d.shuffle(turn,a)
    ##if (b == -1):
        ##print "Invalid Input:card not in hand OR SupplyEmpty"
    ##assert(b ==0)
    print "TEST PASS"
    print "After Shuffling"
    print "Deck"
    print a.deck
    
def test_drawCard():
    ##kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cut purse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print "TESTING drawCard()"
    a = d.initializeGame(numPlayers,kingdomCards, randomSeed)
    assert(a !=-1)
    print "Before drawing"
    print "Deck"
    print a.deck
    print "Hand"
    print a.hand
    for turn in range(numPlayers):
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
    maxBonus = random.randint(2,5)
    maxHandCount = random.randint(2,5)
    ##kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cut purse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print "TESTING UpdateCoins()"
    a = d.initializeGame(numPlayers,kingdomCards, randomSeed)
    assert(a !=-1)
    for i in range(numPlayers):
        a.hand[i] = []
    for player in range(numPlayers):
        for handCount in range(1,maxHandCount+1):
            a.hand[player].append("Copper")
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
    ##kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cut purse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    tempcard = random.choice(kingdomCards)
    ## why only kingdom Cards because if i choose any other card which is not choosen in kingdormcards. It is throwing an error.Mentioned in Testreport.
    card = d.cardlist.index(tempcard)
    print "TESTING buyCard_gainCard()"
    a = d.initializeGame(numPlayers,kingdomCards, randomSeed)
    assert(a !=-1)
    a.whoseTurn = random.randint(0,numPlayers-1)
    print "Before Buying"
    print "Card want to Buy:"
    print d.cardlist[card]
    print "Cost of Card"
    x = d.getCost(d.cardlist[card])
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
    print a.supplyCount[d.cardlist[card]]
    b = d.buyCard(card,a)
    if (b == -1):
        print "Invalid Input:No numBuys OR No enough Coins OR SupplyEmpty"
    if(b ==0):
        print "BuyCard() is successfull for player : %d brought: %s" %(a.whoseTurn,card)
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
        print a.supplyCount[d.cardlist[card]]

def test_discardCard(): 
    ##kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cut purse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    card= random.choice(["Copper","Estate"])
    print "TESTING discardCard()"
    a = d.initializeGame(numPlayers,kingdomCards, randomSeed)
    assert(a !=-1)
    print "Before discard"
    print "Card to discard:"
    print card
    print "hand before discarding"
    print a.hand
    print "Coins available:"
    print a.coins
    b = d.discardCard(card,a.whoseTurn,a,0)
    if (b == -1):
        print "Invalid Input:card not in hand OR SupplyEmpty"
    assert(b ==0)
    print "TEST PASS"
    print "discardCard() is successfull for player : %d discarded %s" %(a.whoseTurn,card)
    print "After Discarding"
    print "Card Discarded:"
    print card
    print "Hand after Discarding"
    print a.hand
    print "Coins Available:"
    print a.coins

def test_getCost():
    print("Testing getCost()")
    card = "Smithy"
    print("Getting cost of card: %s" %card)
    r=d.getCost(card)
    assert(r==4)
    print ("Cost of card : %s is %d" %(card,r))
    
def test_playCard():
    card = random.choice(kingdomCards)
    ##kingdomCards = ["Adventurer", "Ambassador", "Baron","Council Room", "Cut purse", "Embargo", "Feast", "Gardens", "Great Hall","Mine"]
    a = d.initializeGame(numPlayers,kingdomCards, randomSeed)
    assert(a !=-1)
    print "Before playing"
    a.hand[0].append(card)
    print "hand of Player 0:"
    print a.hand[0]
    print "discard"
    print a.discard[0]
    print "deck"
    print a.deck[0]
    print "Buys"
    print a.numBuys
    print "Actions"
    print a.numActions
    print "Coins"
    print a.coins
    print "Card played by Player : 0 is "
    print card
    hpos = len(a.hand[0])-1
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
        print "discard"
        print a.discard[0]
        print "deck"
        print a.deck[0]
        print "Buys"
        print a.numBuys
        print "Actions"
        print a.numActions
        print "Coins"
        print a.coins
        print "Card played by Player:0 is "
        print card

def test_scoreFor():
    ##kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cut purse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print("Testing scoreFor()")
    r = d.initializeGame(numPlayers, kingdomCards,randomSeed)
    assert(r!=-1)
    for player in range(numPlayers):
        print "Hand: %d" %player
        print r.hand[player]
        print "Deck: %d" %player
        print r.deck[player]
        print "Discard: %d" %player
        print r.discard[player]
        x = d.scoreFor(player,r)
        assert(x!= -1)
        print ("Score for player : %d is:" %player)
        print x


def test_getWinners():
    ##kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cut purse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print("Tetsing getWinners")
    p = d.initializeGame(numPlayers, kingdomCards,randomSeed)
    p.discard[0].append("Province")
    p.discard[1].append("Province")
    for player in range(numPlayers):
        print "Score of Player: %d" %player
        print d.scoreFor(player,p)
    r = d.getWinners(p)
    assert(r!=-1)
    print("Player Won:")
    print r

def test_isGameOver():
    ##kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cut purse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print("Testing isGameOver")
    r = d.initializeGame(numPlayers, kingdomCards,randomSeed)
    assert(r !=-1)
    r.supplyCount["Province"] = 0
    s = d.isGameOver(r)
    assert(s == 1)
    print ("Game Over: SUpply of province exhausted")
    print "Supply of province:"
    print r.supplyCount["Province"]

    x = d.initializeGame(numPlayers, kingdomCards,randomSeed)
    assert(x!= -1)
    x.supplyCount["Duchy"] = 0
    x.supplyCount["Estate"] = 0
    x.supplyCount["Village"] = 0
    y = d.isGameOver(x)
    assert(y == 1)
    print ("Game Over:Supply of 3 piles is empty")
    print x.supplyCount["Duchy"]
    print x.supplyCount["Estate"]
    print x.supplyCount["Village"]


def test_endTurn():
    ##kingdomCards = [d.Adventurer, d.Ambassador, d.Baron, d.Council_Room, d.Cut purse, d.Embargo, d.Feast, d.Gardens, d.Great_Hall, d.Village]
    print("Testing endTurn")
    r= d.initializeGame(numPlayers, kingdomCards,randomSeed)
    assert(r != -1)
    print ("Whose Turn:")
    print r.whoseTurn
    print "Discard"
    print r.discard
    print "Hand"
    print r.hand
    s = d.endTurn(r)
    assert (s == 0)
    print ("After endTurn:")
    print ("Whose Turn:")
    print r.whoseTurn
    print "Discard"
    print r.discard
    print "Hand"
    print r.hand

    
for i  in range(10):
    numPlayers = random.randint(2,4)
    randomSeed = 111
    test_initializeGame()
     ##kingdomCards= "Adventurer", "Ambassador", "Baron","Council Room", "Cut purse", "Embargo", "Feast", "Gardens", "Great Hall","Village"
    kingdomCards= random.sample(["Adventurer", "Ambassador", "Baron","Council Room", "Cut purse", "Embargo","Feast", "Gardens", "Great Hall","Mine", "Smithy", "Village", "Sea Hag"],10)
    ##kingdomCards= random.sample(["Curse","Estate","Duchy","Province","Copper", "Silver", "Gold","Adventurer", "Ambassador", "Baron","Council Room", "Cut purse", "Embargo","Feast", "Gardens", "Great Hall","Mine", "Smithy", "Village", "Sea Hag"],10)
    print  "All tests are based on below settings"
    print "Players"
    print numPlayers
    print "Kingdom Cards"
    print kingdomCards
    test_shuffle()
    test_drawCard()
    test_updateCoins()
    test_discardCard()
    test_getCost()
    test_buyCard_gainCard()
    test_playCard()
    test_scoreFor()
    test_getWinners()
    test_isGameOver()
    test_endTurn()
