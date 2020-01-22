#pragma once
#include "Vector2.h"
#include "Matrix22h.h"

// Class representing a 2D homogeneous vector
// This contains some of the most common vector operations -- feel free to extend it
class Vector2h
{
public:
	// Default constructor
	Vector2h() : x(0.0f), y(0.0f), w(0.0f) {}

	// Constructor to initialise from a Vector2
	Vector2h(const Vector2& vec) : x(vec.x), y(vec.y), w(1.0f) {}

	// Converts back to a Vector2
	Vector2 asVector2() const
	{
		return Vector2(x, y);
	}

	// The three components of the homogeneous vector
	// NB w should always be 1 (for now...).
	float x, y, w;
};

// Matrix multiplication operator (matrix * vector)
// NB since the Vector2h is the second operand, this can't be defined as a method inside the Vector2h class
inline Vector2h operator*(const Matrix22h& m, const Vector2h& v)
{
	// TO DO
	Vector2h result;
	return result;
}