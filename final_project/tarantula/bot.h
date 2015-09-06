#ifndef __BOT_H
#define __BOT_H
#include "dominion.h"
#include "interface.h"
#include "dominion_helpers.h"
#include "rngs.h"
#include "printState.h"
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>


#define hand_size 5

int playHand(struct gameState *game);
int randAction(struct gameState *game);
int randBuy(struct gameState *game);
int doAction(int card, int handPos, int currentPlayer, struct gameState *game);

#endif
