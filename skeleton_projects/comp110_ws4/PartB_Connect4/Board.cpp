#include "stdafx.h"
#include "Board.h"

Board::Board(int width, int height)
	: width(width), height(height)
{
	contents = new int[width * height];

	for (int x = 0; x < width; x++)
		for (int y = 0; y < height; y++)
			setSquare(x, y, 0);
}

Board::~Board()
{
	delete contents;
}

int Board::getSquare(int x, int y)
{
	if (x < 0 || x >= width || y < 0 || y >= height)
		throw OutOfBoardError();
	else
		return contents[y*width + x];
}

void Board::setSquare(int x, int y, int value)
{
	if (x < 0 || x >= width || y < 0 || y >= height)
		throw OutOfBoardError();
	else
		contents[y*width + x] = value;
}

void Board::print()
{
	for (int y = 0; y < height; y++)
	{
		for (int x = 0; x < width; x++)
		{
			switch (getSquare(x,y))
			{
			case 0:
				std::cout << ".";
				break;
			case 1:
				std::cout << "1";
				break;
			case 2:
				std::cout << "2";
				break;
			default:
				std::cout << "?";
				break;
			}
		}
		std::cout << std::endl;
	}
}

// TODO: uncomment and implement
/* bool Board::performMove(int player, int x)
{
} */

// TODO: uncomment and implement
/* int Board::checkLine(int startX, int startY, int dirX, int dirY)
{
} */

// TODO: uncomment and implement
/* int Board::checkWin()
{
}*/

