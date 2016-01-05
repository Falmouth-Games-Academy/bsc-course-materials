#include "stdafx.h"

#include "words.h"

char getLetter()
{
	while (true)
	{
		std::cout << "Enter a letter: ";
		std::string line;
		std::getline(std::cin, line);

		if (line.length() == 1 && isalpha(line[0]))
		{
			return toupper(line[0]);
		}
		else
		{
			std::cout << "That's not a letter!" << std::endl;
		}
	}
}

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
	while (true)
	{
		char letter = getLetter();
		std::cout << "You entered " << letter << std::endl;
	}

	return 0;
}

