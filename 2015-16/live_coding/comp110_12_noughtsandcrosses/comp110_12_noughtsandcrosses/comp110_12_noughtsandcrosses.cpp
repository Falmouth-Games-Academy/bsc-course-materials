// comp110_12_noughtsandcrosses.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

const int boardSize = 3;

enum SquareContents
{
	scEmpty,
	scNought,
	scCross
};

SquareContents board[boardSize][boardSize];

void clearBoard()
{
	for (int x = 0; x < boardSize; x++)
	{
		for (int y = 0; y < boardSize; y++)
		{
			board[x][y] = scEmpty;
		}
	}
}

void printBoard()
{
	for (int y = 0; y < boardSize; y++)
	{
		// Output the horizontal lines
		if (y > 0)
		{
			for (int x = 0; x < boardSize; x++)
			{
				if (x > 0)
					std::cout << "+";

				std::cout << "-";
			}

			std::cout << std::endl;
		}

		// Output the row contents
		for (int x = 0; x < boardSize; x++)
		{
			if (x > 0)
				std::cout << "|";

			switch (board[x][y])
			{
			case scEmpty:
				std::cout << ".";
				break;

			case scNought:
				std::cout << "O";
				break;

			case scCross:
				std::cout << "X";
				break;

			default:
				std::cout << "?";
				break;
			}
		}

		std::cout << std::endl;
	}
}

void getMove(int& out_x, int& out_y, int currentPlayer)
{
	for (;;)
	{
		std::cout << "Player " << currentPlayer << ", enter a move: ";
		std::string line;
		std::getline(std::cin, line);

		if (line.length() == 2)
		{
			if (isdigit(line[0]) && isdigit(line[1]))
			{
				out_x = line[0] - '0';
				out_y = line[1] - '0';

				if (out_x < 0 || out_x >= boardSize)
				{
					std::cout << "Move is outside board" << std::endl;
					continue;
				}
				else if (out_y < 0 || out_y >= boardSize)
				{
					std::cout << "Move is outside board" << std::endl;
					continue;
				}
				else if (board[out_x][out_y] != scEmpty)
				{
					std::cout << "Square is not empty" << std::endl;
					continue;
				}
				else
				{
					return;
				}
			}
		}

		std::cout << "Invalid input" << std::endl;
	}
}

void playMove(int x, int y, int currentPlayer)
{
	if (currentPlayer == 1)
		board[x][y] = scNought;
	else if (currentPlayer == 2)
		board[x][y] = scCross;
	else
		std::cout << "Invalid currentPlayer" << std::endl;
}

SquareContents checkLine(int x, int y, int dx, int dy)
{
	if (board[x][y] == scEmpty)
		return scEmpty;

	for (int i = 1; i < boardSize; i++)
	{
		if (board[x+i*dx][y+i*dy] != board[x][y])
		{
			return scEmpty;
		}
	}

	return board[x][y];
}

SquareContents getWinner()
{
	SquareContents winner = scEmpty;

	// Horizontal lines
	for (int y = 0; y < boardSize; y++)
	{
		winner = checkLine(0, y, 1, 0);
		if (winner != scEmpty) return winner;
	}

	// Vertical lines
	for (int x = 0; x < boardSize; x++)
	{
		winner = checkLine(x, 0, 0, 1);
		if (winner != scEmpty) return winner;
	}

	// Diagonal lines
	winner = checkLine(0, 0, 1, 1);
	if (winner != scEmpty) return winner;

	winner = checkLine(0, boardSize - 1, 1, -1);
	if (winner != scEmpty) return winner;

	return scEmpty; // no winner yet
}

int main()
{
	clearBoard();

	printBoard();

	int currentPlayer = 1;

	for (;;)
	{
		int x, y;
		getMove(x, y, currentPlayer);
		std::cout << "Chosen move is " << x << ", " << y << std::endl;

		playMove(x, y, currentPlayer);

		printBoard();

		int winner = getWinner();
		if (winner != 0)
		{
			std::cout << "Player " << winner << " wins!" << std::endl;
			break;
		}

		//currentPlayer = (currentPlayer == 1) ? 2 : 1;
		currentPlayer = 3 - currentPlayer;
	}

    return 0;
}

