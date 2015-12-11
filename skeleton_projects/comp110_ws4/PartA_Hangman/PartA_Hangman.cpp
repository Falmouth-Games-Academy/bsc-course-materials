#include "stdafx.h"

#include "words.h"

// TODO: uncomment and implement this function
/*
char getLetter()
{
}
*/

// TODO: uncomment and implement this function
/*
std::string fillInLetter(std::string partialWord, std::string secretWord, char letter)
{
}
*/

int main()
{
	// Seed the random number generator with the current time,
	// to ensure different results each time the program is run
	srand(static_cast<unsigned int>(time(nullptr)));
	
	// Choose the secret word
	std::string secretWord = chooseRandomWord();

	// Construct a string of dashes, the same length as the secret word
	std::string partialWord(secretWord.length(), '-');

	// TODO: implement the main game loop

	return 0;
}

