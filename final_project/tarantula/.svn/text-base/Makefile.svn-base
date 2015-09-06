CFLAGS = -Wall -fpic -coverage -lm
TESTS = testSuite.c unittest4.o unittest3.o unittest2.o unittest1.o cardtest1.o cardtest2.o cardtest3.o cardtest4.o
STANDARD = dominion.o rngs.o printState.o
RANDTESTS = randcard.h randstategen.o
all= vaseka anderma2 almeidam menardd toyj run doOneHundredTimes doTenTimes doOnce playGame 
.PHONY: $(all)



tarantula:
	-@bash -c "mkdir tarantulaOut"
	@echo 21718281828 > Seed.txt
	@bash -c "cd .. ; cp ../vaseka/dominion.c ./tarantula/dominion.c"
	-@bash -c "cp ./tarantulaOut/tally.txt ./tally.txt"

	@make oneHundredTarantula -s

	@make oneHundredTarantula -s

	@make oneHundredTarantula -s

	@bash -c "mv ./tarantula.out ./tarantulaOut/tarantula.out"
	@bash -c "mv ./tally.txt ./tarantulaOut/tally.txt"
	@make clean
	-@rm -f dominion.c.gcov

testdominion: testdominion.c  bot.o $(STANDARD)
	gcc -o testdominion -g testdominion.c bot.o $(STANDARD) $(CFLAGS)



bot.o: bot.c bot.h $(STANDARD)
	gcc -c bot.c -g $(CFLAGS)

printState.o: printState.c printState.h
	gcc -c printState.c -g $(CFLAGS)

rngs.o: rngs.h rngs.c
	gcc -c rngs.c -g  $(CFLAGS)

dominion.o: dominion.h dominion.c rngs.o
	gcc -c dominion.c -g  $(CFLAGS)

clean:
	rm -f *.o *.gcda *.gcno *.so testdominion dominion.c Seed.txt tally.txt dominion.c.gcov temp.out


oneHundredTarantula:
	make tenTarantula
	make tenTarantula
	make tenTarantula
	make tenTarantula
	make tenTarantula
	make tenTarantula
	make tenTarantula
	make tenTarantula
	make tenTarantula
	make tenTarantula


tenTarantula:
	make oneTarantula
	make oneTarantula
	make oneTarantula
	make oneTarantula
	make oneTarantula
	make oneTarantula
	make oneTarantula
	make oneTarantula
	make oneTarantula
	make oneTarantula

oneTarantula:
	-rm -f dominion.o dominion.gcno dominion.gcda dominion.c.gcov
	make dominion.o
	-rm -f tarantula.out
	-make tarantulaHelper
	-gcov dominion.c > temp.out
	python tarantula.py

tarantulaHelper: testdominion bot.o $(STANDARD)
	timeout 10s ./testdominion > temp.out
	gcov dominion.c > temp.out
	python tarantula.py yes
