import random
import dominion as d
def test_InitializeGame():
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
    
for i in range(10):
    test_InitializeGame()
