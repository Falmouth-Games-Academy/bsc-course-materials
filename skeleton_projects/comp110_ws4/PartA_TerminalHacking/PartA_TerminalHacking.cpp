// PartA_TerminalHacking.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

// Read all words of the specified length
std::vector<std::string> readWords(int length)
{
	std::cout << "Reading word list" << std::endl;

	std::vector<std::string> words;

	std::ifstream wordFile("words.txt");
	std::string word;

	// Read past the copyright notice at the top of words.txt
	while (std::getline(wordFile, word) && word != "---")
	{
		// do nothing
	}

	// Read each line in the file
	while (std::getline(wordFile, word))
	{
		if (word.length() == length)
		{
			// Scan through the line, converting each character to upper case.
			// If a non-alphabet character is encountered, reject the word.
			bool isValid = true;
			for (int i = 0; i < word.length(); i++)
			{
				if (isalpha(word[i]))
				{
					word[i] = toupper(word[i]);
				}
				else
				{
					isValid = false;
					break;
				}
			}

			// If it's a good word, add it to the list.
			if (isValid)
			{
				words.push_back(word);
			}
		}
	}

	std::cout << "Found " << words.size() << " words" << std::endl;

	return words;
}


int main()
{
	readWords(5);

    return 0;
}

