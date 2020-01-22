#pragma once
#include "Matrix22.h"

// Class representing a 2x2 homogeneous matrix
// This contains some of the most common matrix operations -- feel free to extend it
class Matrix22h
{
public:
	// Default constructor
	Matrix22h() {}

	// Constructor to initialise from a Matrix22
	Matrix22h(const Matrix22& mat) :
		m11(mat.m11), m12(mat.m12), m21(mat.m21), m22(mat.m22) {}

	// The 9 components in row order... NB the last row and column should always be
	// 0 except for m33, which should always be 1.
	float m11 = 0.0f,
		m12 = 0.0f,
		m13 = 0.0f,
		m21 = 0.0f,
		m22 = 0.0f,
		m23 = 0.0f,
		m31 = 0.0f,
		m32 = 0.0f,
		m33 = 1.0f;

	// Set this matrix to be the identity matrix
	void setIdentity()
	{
		m11 = m22 = m33 = 1.0f;
		m12 = m13 = m21 = m23 = m31 = m32 = 0.0f;
	}

	// Returns the result AB of multiplying this homogeneous matrix (A) by another (B)
	Matrix22h operator*(const Matrix22h& other) const
	{
		// TO DO
		Matrix22h m;
		return m;
	}
};