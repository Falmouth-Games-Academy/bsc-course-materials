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

	//std::cout << secretWord << std::endl;

	int lives = 14;

	while (true)
	{
		std::cout << partialWord << std::endl;
		std::cout << "You have " << lives << " lives left" << std::endl;

		char letter = getLetter();
		std::cout << "You entered " << letter << std::endl;

		bool found = false;
		for (int i = 0; i < secretWord.length(); i++)
		{
			if (secretWord[i] == letter)
			{
				partialWord[i] = letter;
				found = true;
			}
		}

		if (!found)
		{
			lives--;
			if (lives <= 0)
			{
				std::cout << "You lose :( The word was " << secretWord << std::endl;
				break;
			}
		}

		if (partialWord == secretWord)
		{
			std::cout << "You win!!! The word was " << secretWord << std::endl;
			break;
		}
	}

	return 0;
}

