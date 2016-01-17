#pragma once

class OutOfBoardError : std::exception
{
};

// Represents a Connect 4 board
class Board
{
public:
	Board(int width, int height);
	~Board();

	// Print the board to the console window
	void print();

	// Get the contents of a square on the board: 1 or 2 for the corresponding player, or 0 for an empty square
	// x=0 y=0 is the top left corner of the board
	int getSquare(int x, int y);

	// Drop a counter into the given column
	// Returns true if the move is played successfully, false if not (i.e. if the column is full)
	bool performMove(int player, int x);

	// Check if either player has won the game
	// Returns 1 or 2 if the corresponding player has won, or 0 if there is no winner yet
	int checkWin();

private:
	int width, height;
	int* contents;

	// Set the contents of a square on the board
	void setSquare(int x, int y, int value);

	// Check for a single line on the board, starting at (startX, startY) in the direction (dirX, dirY)
	// Returns 1 or 2 if the corresponding player has made 4 in a row along this line, or 0 otherwise
	int checkLine(int startX, int startY, int dirX, int dirY);
};

