#include <stdio.h>
#include "dominion.h"
#include "printState.h"



void printState(struct gameState *game){
  int i,j;

  printf("Current Game:\n\r");
  printf("Number of Players: %d\n\r",game->numPlayers);

  printf("Non - Kingdom Cards: ");
  for (i=curse;i<=gold;i++) {
    if(game->supplyCount[i]>0){
      printf(" ");
      printCard(i);
    }
  }
  printf("\n\r");  

  printf("Kingdom Cards: ");
  for (i=adventurer;i<=treasure_map;i++) {
    if(game->supplyCount[i]>0){
      printf(" ");
      printCard(i);
    }
  }

  printf("\n\r");

  printf("Outpost Played: %d\n\r",game->outpostPlayed);
  printf("Outpost Turn: %d\n\r",game->outpostTurn);

  printf("Turn: %d\n\r",game->whoseTurn);
  printf("Phase: %d\n\r",game->phase);
  printf("Actions: %d\n\r", game->numActions);
  printf("Buys: %d\n\r", game->numBuys);
  printf("Coins: %d\n\r", game->coins);
  for (i=0; i<game->numPlayers; i++) {
    printf("Hand Count for Player %d: %d\n\r",i+1,game->handCount[i]);
    printf("Hand:");
    for (j=0;j<game->handCount[i];j++){
      printf(" ");
      printCard(game->hand[i][j]);
    }
    printf("\n\r");
  }
  for (i=0; i<game->numPlayers; i++) {
    printf("Deck Count for Player %d: %d\n\r",i+1, game->deckCount[i]);
    printf("Deck:");
    for (j=0;j<game->deckCount[i];j++){
      printf(" ");
      printCard(game->deck[i][j]);
    }
    printf("\n\r");
  }
  for (i=0; i<game->numPlayers; i++) {
    printf("Discard Count for Player %d: %d\n\r",i+1,game->discardCount[i]);
    printf("Discard:");
    for (j=0;j<game->discardCount[i];j++){
      printf(" ");
      printCard(game->discard[i][j]);
    }
    printf("\n\r");
  }
  printf("Number of Played Cards: %d\n\r", game->playedCardCount);
  printf("Played Cards:");
  for (j=0;j<game->playedCardCount;j++){
    printf(" ");
    printCard(game->playedCards[j]);
  }
  printf("\n\r");
}


void printPlayer(struct gameState *game, int player){
  int i;
  printf("Player: %d\n\r",player+1);

  printf("Hand:");
  for (i=0;i<game->handCount[player];i++)
    printf("\t%d",game->hand[player][i]);
  printf("\n\rDeck:");
  for (i=0;i<game->deckCount[player];i++)
    printf("\t%d",game->deck[player][i]);
  printf("\n\rDiscard:");
  for (i=0;i<game->discardCount[player];i++)
    printf("\t%d",game->discard[player][i]);
  printf("\n\r");
}

void printCard(int card){
  switch(card)
    {
    case curse: printf("Curse");
      break;
    case estate: printf("Estate");
      break;
    case duchy: printf("Duchy");
      break;
    case province: printf("Province");
      break;
    case copper: printf("Copper");
      break;
    case silver: printf("Silver");
      break;
    case gold: printf("Gold");
      break;
    case adventurer: printf("Adventurer");
      break;
    case council_room: printf("Council Room");
      break;
    case feast: printf("Feast");
      break;
    case gardens: printf("Gardens");
      break;
    case mine: printf("Mine");
      break;
    case remodel: printf("Remodel");
      break;
    case smithy: printf("Smithy");
      break;
    case village: printf("Village");
      break;
    case baron: printf("Baron");
      break;
    case great_hall: printf("Great Hall");
      break;
    case minion: printf("Minion");
      break;
    case steward: printf("Steward");
      break;
    case tribute: printf("Tribute");
      break;
    case ambassador: printf("Ambassador");
      break;
    case cutpurse: printf("Cutpurse");
      break;
    case embargo: printf("Embargo");
      break;
    case outpost: printf("Outpost");
      break;
    case salvager: printf("Salvager");
      break;
    case sea_hag: printf("Sea Hag");
      break;
    case treasure_map: printf("Treasure Map");
      break;
    default: printf("%d",card);
      break;
    }
}



void printSupply(struct gameState *game) {
  int i;
  for (i=curse;i<=treasure_map;i++) {
    printf("Supply of ");
    printCard(i);
    printf(" is: %d\n\r", game->supplyCount[i]);
  }
}
