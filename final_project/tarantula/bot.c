#include "bot.h"
#include <math.h>

int hasNegative(struct gameState *game);

int playHand(struct gameState *game){

  if(isGameOver(game)) {
    return 0;
  }

  if(hasNegative(game)) {
    printf("Negative card count\n\r");
    return -1;
  }


  int i, count, retVal,player = whoseTurn(game);

  printf("Current Player: %d\n\r",player+1);

  game->phase=0;

  count = 0;
  while(game->handCount[player]<hand_size){
    if(hasNegative(game)) {
      printf("Error encountered: Negative card count\n\r");
      return -1;
    }
    retVal = drawCard(player,game);
    if (retVal != 0) {
      if (game->deckCount[player]+game->discardCount[player] == 0)
	break;
      else {
	printf("Error encountered in previous draw card!\n\r");
	return -1;
      }
    }
    if(count++ > MAX_HAND) {
      printf("Error encountered in previous draw card!\n\r");
      printf("Too many draw cards!\n\r");
      return -1;
    }
  }
  printf("Cards in hand: ");
  count = 0;
  for(i=0;i<game->handCount[player]; i++) {
    printCard(game->hand[player][i]);
    printf("\t");
  }

  printf("\n\r");

  count = 0;
  while(game->numActions > 0) {
    if(hasNegative(game)) {
      printf("Error encountered: Negative card count\n\r");
      return -1;
    }
    retVal = randAction(game);
    if (retVal != 0){
      printf("Error encountered in previous action!\n\r");
      return -1;
    }
    if(count++ > MAX_HAND) {
      printf("Error encountered in previous action!\n\r");
      printf("Too many actions tried!\n\r");
      return -1;
    }
  }
  count = 0;
  while(game->numBuys > 0){
    if(hasNegative(game)) {
      printf("Error encountered: Negative card count\n\r");
      return -1;
    }
    retVal = randBuy(game);
    if (retVal != 0){
      printf("Error encountered in previous buy!\n\r");
      printSupply(game);
      return -1;
    }
    if(count++ > MAX_HAND) {
      game->numBuys=0;
      /*
      printf("Error encountered in previous buy!\n\r");
      printf("Too many buys!\n\r");
      printSupply(game);
      return -1;
      */
    }
  }
  
  if(!isGameOver(game)){
    printf("End of turn\n\r");
    printf("-----------------------------------------------------------\n\r");
    endTurn(game);
  }
  if(hasNegative(game)) {
    printf("Error encountered: Negative card count\n\r");
    return -1;
  }
  
  return 0;
}

int randAction(struct gameState *game) {
  int retVal=0, handPos,currentPlayer;

  currentPlayer = game->whoseTurn;

  for(handPos=0; handPos < game->handCount[currentPlayer]; handPos++)
    if (handCard(handPos, game) >= adventurer)
      break;
  
  if (handPos != game->handCount[currentPlayer]) {
    retVal = doAction(handCard(handPos,game),handPos,currentPlayer,game);
    discardCard(handPos, currentPlayer, game, 0);
  }
  else
    game->numActions = 0;
  return retVal;
}




int doAction(int card, int handPos,int currentPlayer, struct gameState *game) {
  printf("Action: ");
  printCard(card);
  int i,choice1,choice2,choice3, goodRetVal, count;

  choice1 = floor(1000.*Random()-500.);
  choice2 = floor(1000.*Random()-500.);
  choice3 = floor(1000.*Random()-500.);
  goodRetVal = 0;

  switch (card)
    {
    case feast:
      choice1 = floor((treasure_map+1.)*Random());
      /*
	Earlier reported bug
      */
      if(getCost(choice1)>5 || game->supplyCount[choice1] <= 0)
	goodRetVal = -1;
      
      printf("\tCard to gain: ");
      printCard(choice1);
      
      break;


    case gardens:
      goodRetVal = -1;
      break;

    case mine: 
      /* choice1 is hand# of money to trash, choice2 is supply# of
	 money to put in hand */
      for (i=0;i<game->handCount[currentPlayer];i++) {
	if (game->hand[currentPlayer][i] == silver ||
	    game->hand[currentPlayer][i] == copper) {
	  choice1 = i;
	  break;
	}
      }
      choice2 = game->hand[currentPlayer][choice1]+1;
      if(choice2 != game->hand[currentPlayer][choice1]+1 || ((choice2 != gold)&&(choice2!=silver)))
	goodRetVal = -1;
      printf("\tCard to trash: ");
      printCard(game->hand[currentPlayer][choice1]);
      printf("\tCard to gain: ");
      printCard(choice2);
      break;

    case remodel:
      /* choice1 is hand# of card to remodel, choice2 is supply# */
      count = 0;
      do {
	choice1 = floor(Random()*(game->handCount[currentPlayer]));
	if(count++ > MAX_HAND) {
	  return 0;
	}
      } while (choice1 == handPos);
      choice2 = floor(Random()*(treasure_map)+1.);

      if (getCost(choice2) > (2+getCost(game->hand[currentPlayer][choice1])))
	goodRetVal = -1;


      printf("\tCard to remodel: ");
      printCard(game->hand[currentPlayer][choice1]);
      printf("\tCard to gain: ");
      printCard(choice2);
      break;

    case baron: 
      /* choice1: boolean for discard of estate */
      /* Discard is always of first (lowest index) estate */
      choice1= (Random()>0.2);
      /*
      for(i=0;i<game->handCount[currentPlayer];i++)
	if(game->hand[currentPlayer][i]==estate && (Random() < 0.2))
	  choice1=1;
      */
      if (choice1)
	printf("\tDiscard first estate");
      else
	printf("\tDo not discard");
      break;


    case minion: /* choice1:  1 = +2 coin, 2 = redraw */
      choice1 = 1;
      choice1 += floor(Random()*2);
      if (choice1 == 1)
	printf("\tGain two coins");
      else
	printf("\tRedraw");
      break;

    case steward: /* choice1: 1 = +2 card, 2 = +2 coin, 3 = trash 2 (choice2,3) */
      choice1 = floor(Random()*3+1);
      if (choice1==3){
	if (game->handCount[currentPlayer] < 3)
	  choice1 = floor(Random()*2+1);
	else { 
	  count = 0;
	  do {
	    choice2 = floor(Random()*(game->handCount[currentPlayer]));
	    choice3 = floor(Random()*(game->handCount[currentPlayer]));
	    if(count++ > MAX_HAND) {
	      return 0;
	    }
	  } while (choice2 == handPos || choice3 == handPos || choice2 == choice3);
	}
      }
      switch (choice1)
	{
	case 1:
	  printf("\tGain two cards");
	  break;
	case 2:
	  printf("\tGain two coins");
	  break;
	case 3:
	  printf("\tTrash two cards: ");
	  printCard(game->hand[currentPlayer][choice2]);
	  printf("\t");
	  printCard(game->hand[currentPlayer][choice3]);
	  break;
	}
      break;

    case ambassador: /* choice1 = hand#, choice2 = number to return to supply */
      count = 0;
      do {
	choice1 = floor(Random()*(game->handCount[currentPlayer]));
	if(count++ > MAX_HAND) {
	  return 0;
	}
      } while (choice1 == handPos);
      choice2 = -1;
      for (i=0; i<game->handCount[currentPlayer]; i++)
	if (game->hand[currentPlayer][i] == game->hand[currentPlayer][choice1])
	  choice2++;
      if (choice2 > 2)
	choice2 = 2;
      printf("\tCard to return: ");
      printCard(game->hand[currentPlayer][choice1]);
      printf("\tNumber to return: %d", choice2);
      break;

    case embargo: /* choice1 = supply# */
      count = 0;
      do {
	choice1 = floor(Random()*treasure_map+1);
	if (count++ > MAX_HAND){
	  goodRetVal = -1;
	  break;
	}
      }while(game->supplyCount[choice1] < 0);
      printf("\tEmbargo on: ");
      printCard(choice1);
      break;

    case salvager: /* choice1 = hand# to trash */
      count = 0;
      do {
	choice1 = floor(Random()*(game->handCount[currentPlayer]));
	if(count++ > MAX_HAND) {
	  return 0;
	}
      } while (choice1 == handPos);

      printf("\tCard to salvage: ");
      printCard(game->hand[currentPlayer][choice1]);
      break;

    case treasure_map:
      goodRetVal = -1;
      for (i=0; i<game->handCount[currentPlayer]; i++)
	if (i != handPos)
	  if (game->hand[currentPlayer][i] == treasure_map)
	    goodRetVal=0;
      break;

    default: 
      /*adventurer, council_room, smithy, village, great_hall, \
	tribute, cutpurse, outpost, sea_hag*/
      break;
    }
  
  printf("\r\n");

  int actual;
  actual = playCard(handPos,choice1,choice2,choice3,game);


  if(goodRetVal == actual)
    return 0;
  printf("Expected: %d, Got: %d\n\r",goodRetVal,actual);
  return -1;
}



int randBuy(struct gameState *game){
  int card;
  if (game->coins >= getCost(province))
    card = province;
  else
    card = floor(Random()*(treasure_map+1));

  if (game->coins == 0){
    game->numBuys = 0;
    return 0;
  }


  if (getCost(card) > game->coins || game->supplyCount[card] <= 0) {
    if (buyCard(card,game) == 0) {
      printf("Bad attempt to buy card was successfull: ");
      printCard(card);
      printf("\n\r");
      return -1;
    }
    else
      return 0;
  }


  printf("Card to buy: ");
  printCard(card);
  printf("\n\r");
  return buyCard(card,game);
}



int hasNegative(struct gameState *game) {
  int i;

  for (i=0;i<game->numPlayers;i++){
    if (game->handCount[i] < 0)
      return 1;
    if (game->deckCount[i] < 0)
      return 1;
    if (game->discardCount[i] < 0)
      return 1;
  }

  return 0;
}
