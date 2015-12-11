// This file contains functions for working with a list of words read
// from a text file. You do not need to modify anything in here.

#include "stdafx.h"

// The list of words to choose from.
// Words consist of the characters A-Z (upper case) only.
std::vector<std::string> words;

// Read the list of words from words.txt
void readWords()
{
	std::cout << "Reading word list" << std::endl;

	std::ifstream wordFile("words.txt");
	std::string line;

	// Read past the copyright notice at the top of words.txt
	while (std::getline(wordFile, line) && line != "---")
	{
		// do nothing
	}

	// Read each line in the file
	while (std::getline(wordFile, line))
	{
		bool isValid = true;

		// Scan through the line, converting each character to upper case.
		// If a non-alphabet character is encountered, reject the word.
		std::string word;
		for each (char c in line)
		{
			if (isalpha(c))
			{
				word.append(1, toupper(c));
			}
			else
			{
				isValid = false;
				break;
			}
		}

		// If it's a good word, add it to the list.
		if (isValid && word.length() > 2)
		{
			words.push_back(word);
		}
	}

	std::cout << "Found " << words.size() << " words" << std::endl;
}

// Choose a random word from the word list
std::string chooseRandomWord()
{
	if (words.empty())
		readWords();

	// Choose a random number between 0 and words.size()-1
	int index = rand() % words.size();

	return words[index];
}

