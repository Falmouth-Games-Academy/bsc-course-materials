#pragma once

// Class representing a 2x2 matrix
// This contains some of the most common matrix operations -- feel free to extend it
class Matrix22
{
public:
	// Default constructor, initialises all components to 0
	Matrix22() : m11(0.0f), m12(0.0f), m21(0.0f), m22(0.0f) {}

	// Constructor initialising the vector from components given in row order
	Matrix22(float a, float b, float c, float d) :
		m11(a), m12(b), m21(c), m22(d) {}

	// The four components of the matrix
	float m11, m12, m21, m22;

	// Set this matrix to be the identity matrix
	void setIdentity()
	{
		m11 = m22 = 1.0f;
		m12 = m21 = 0.0f;
	}

	// Returns the result AB of multiplying this matrix (A) by another (B)
	Matrix22 operator*(const Matrix22& other) const
	{
		// TO DO
		Matrix22 m;
		return m;
	}

	// Returns the inverse (B) of this matrix (A) such that AB = BA = I
	Matrix22 inverse() const
	{
		// TO DO
		Matrix22 m;
		return m;
	}
};