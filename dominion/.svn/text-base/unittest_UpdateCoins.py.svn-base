import random
import dominion as d
def test_UpdateCoins():
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
for i in range(5):
    test_UpdateCoins()
