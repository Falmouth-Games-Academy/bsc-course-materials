#pragma once
#include "Vector2h.h"

// A Shape is a collection of points and lines to be drawn together.
// The points/lines can be stored in any format, but must be returned by the
// getPoints()/getLines() functions so that they can be drawn by the Application.
class Shape
{
public:
	// This function should be implemented by derived classes to populate 'points'
	// with all the x,y values to draw as individual points (formatted as Vector2 values
	// for convenience only)
	virtual void getPoints(std::vector<Vector2>& points) const { points.clear();  }

	// This function should be implemented by derived classes to populate 'lines'
	// with pairs of vectors to draw as lines (without any direction). The first
	// item in each pair should be the vector representing the magnitude and direction
	// of the line vector, while the second should be its start point.
	virtual void getLines(std::vector<std::pair<Vector2, Vector2>>& lines) const { lines.clear();  }

	// These functions should apply the transform described by the given matrix to all points of the shape.
	virtual void applyMatrixTransformation(const Matrix22& m) = 0;
	virtual void applyMatrixTransformation(const Matrix22h& m) = 0;

private:
};

class StickDude : public Shape
{
public:
	StickDude(Vector2 centre = Vector2(0.0f, 0.0f));

	void getPoints(std::vector<Vector2>& points) const;
	void getLines(std::vector<std::pair<Vector2, Vector2>>& lines) const;
	void applyMatrixTransformation(const Matrix22& m);
	void applyMatrixTransformation(const Matrix22h& m);

private:
	Vector2 m_neck = Vector2(0.0f, 1.7f);
	Vector2 m_hips = Vector2(0.0f, 0.0f);
	Vector2 m_left_foot = Vector2(1.0f, -2.0f);
	Vector2 m_right_foot = Vector2(-1.0f, -2.0f);
	Vector2 m_shoulder = Vector2(0.0f, 1.25f);
	Vector2 m_left_hand = Vector2(0.5f, -0.1f);
	Vector2 m_right_hand = Vector2(-1.0f, 2.1f);
	Vector2 m_head1 = Vector2(-0.25f, 1.7f);
	Vector2 m_head2 = Vector2(0.25f, 1.7f);
	Vector2 m_head3 = Vector2(0.25f, 2.2f);
	Vector2 m_head4 = Vector2(-0.25f, 2.2f);
	Vector2 m_bowtie = Vector2(0.0f, 1.35f);
};

class DotBox : public Shape
{
public:
	// Constructor - takes the four vertices a, b, c and d, and the position of the dot, t
	DotBox(Vector2 a = Vector2(0, 0), Vector2 b = Vector2(0, 0), Vector2 c = Vector2(0, 0), Vector2 d = Vector2(0, 0),
		Vector2 t = Vector2(0, 0)) :
		v1(a), v2(b), v3(c), v4(d), dot(t) {}

	void getPoints(std::vector<Vector2>& points) const;
	void getLines(std::vector<std::pair<Vector2, Vector2>>& lines) const;
	void applyMatrixTransformation(const Matrix22& m);
	void applyMatrixTransformation(const Matrix22h& m);

private:
	Vector2 v1, v2, v3, v4, dot;
};