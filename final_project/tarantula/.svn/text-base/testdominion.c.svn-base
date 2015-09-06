#include "bot.h"
#include <math.h>
#include <stdio.h>


int main(int argc, char **argv) {
  struct gameState *game;
  int i,j,round, card, numCards = 0, numPlayers, seed, cards[10], winners[MAX_PLAYERS], retVal;
  FILE *temp;
  char *buffer;
  int lengthBuffer = 7;
  buffer = (char *)malloc(sizeof(char)*lengthBuffer);

  temp = fopen("Seed.txt","r");
  fread(buffer,sizeof(char), lengthBuffer, temp);
  fclose(temp);

  seed = atoi(buffer);
  seed += 111;
  for(i=1, j=lengthBuffer;i<=seed;i*=10)
    buffer[--j]=(char)((seed/i)%10+(int)'0');

  temp = fopen("Seed.txt","w");
  fwrite(buffer,sizeof(char), lengthBuffer, temp);
  fclose(temp);
  
  seed -= 111;

  PutSeed(seed);



  game = newGame();

  numPlayers = floor(Random()*3+2);

  seed = floor(Random()*2147483647);

  while (numCards < 10) {
    card = floor(Random()*(treasure_map-adventurer+1)+adventurer);
    cards[numCards] = card;
    numCards++;
    for(i=0; i < (numCards-1); i++)
      if (card == cards[i])
	numCards--;
  }

  initializeGame(numPlayers, cards, seed, game);

  printf("Starting point of the game\n\r");
  printState(game);

  printf("-----------------------------------------------------------\n\r");

  retVal = 0;
  
  round = 1;

  while(!isGameOver(game) && retVal == 0){
    if (game->whoseTurn == 0)
      printf("\n\rStart of round %d\n\r",round++);
    retVal = playHand(game); 
    if (round > 1000)
      return 0;
  }
  printf("-----------------------------------------------------------\n\r");
  printf("Final Game State\n\r");
  printState(game);


  getWinners(winners,game);
  for (i=0;i<MAX_PLAYERS; i++)
    if(winners[i])
      printf("Winner: %d\n\r",i+1);


  printf("-----------------------------------------------------------\n\r");
  printf("-----------------------------------------------------------\n\r");

  free(game);
  return retVal;
}
