#pragma once

class WordList
{
public:
	WordList(int wordLength);

	std::string getRandomWord();

private:
	std::vector<std::string> words;
};
