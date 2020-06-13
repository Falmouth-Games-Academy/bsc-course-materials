#include "stdafx.h"
#include "Shape.h"

StickDude::StickDude(Vector2 centre)
{
	m_neck = centre + m_neck;
	m_hips = centre + m_hips;
	m_left_foot = centre + m_left_foot;
	m_right_foot = centre + m_right_foot;
	m_shoulder = centre + m_shoulder;
	m_left_hand = centre + m_left_hand;
	m_right_hand = centre + m_right_hand;
	m_head1 = centre + m_head1;
	m_head2 = centre + m_head2;
	m_head3 = centre + m_head3;
	m_head4 = centre + m_head4;
	m_bowtie = centre + m_bowtie;
}

void StickDude::getPoints(std::vector<Vector2>& points) const
{
	points.clear();
	points.push_back(m_bowtie);
}

void StickDude::getLines(std::vector<std::pair<Vector2, Vector2>>& lines) const
{
	lines.clear();
	lines.push_back(std::make_pair(m_neck - m_hips, m_hips));
	lines.push_back(std::make_pair(m_left_foot - m_hips, m_hips));
	lines.push_back(std::make_pair(m_right_foot - m_hips, m_hips));
	lines.push_back(std::make_pair(m_left_hand - m_shoulder, m_shoulder));
	lines.push_back(std::make_pair(m_right_hand - m_shoulder, m_shoulder));
	lines.push_back(std::make_pair(m_head2 - m_head1, m_head1));
	lines.push_back(std::make_pair(m_head3 - m_head2, m_head2));
	lines.push_back(std::make_pair(m_head4 - m_head3, m_head3));
	lines.push_back(std::make_pair(m_head1 - m_head4, m_head4));
}

void StickDude::applyMatrixTransformation(const Matrix22 & m)
{
	m_neck = m * m_neck;
	m_hips = m * m_hips;
	m_left_foot = m * m_left_foot;
	m_right_foot = m * m_right_foot;
	m_shoulder = m * m_shoulder;
	m_left_hand = m * m_left_hand;
	m_right_hand = m * m_right_hand;
	m_head1 = m * m_head1;
	m_head2 = m * m_head2;
	m_head3 = m * m_head3;
	m_head4 = m * m_head4;
	m_bowtie = m * m_bowtie;
}

void StickDude::applyMatrixTransformation(const Matrix22h & m)
{
	m_neck = (m * Vector2h(m_neck)).asVector2();
	m_hips = (m * Vector2h(m_hips)).asVector2();
	m_left_foot = (m * Vector2h(m_left_foot)).asVector2();
	m_right_foot = (m * Vector2h(m_right_foot)).asVector2();
	m_shoulder = (m * Vector2h(m_shoulder)).asVector2();
	m_left_hand = (m * Vector2h(m_left_hand)).asVector2();
	m_right_hand = (m * Vector2h(m_right_hand)).asVector2();
	m_head1 = (m * Vector2h(m_head1)).asVector2();
	m_head2 = (m * Vector2h(m_head2)).asVector2();
	m_head3 = (m * Vector2h(m_head3)).asVector2();
	m_head4 = (m * Vector2h(m_head4)).asVector2();
	m_bowtie = (m * Vector2h(m_bowtie)).asVector2();
}

void DotBox::getPoints(std::vector<Vector2>& points) const
{
	points.clear();
	points.push_back(dot);
}

void DotBox::getLines(std::vector<std::pair<Vector2, Vector2>>& lines) const
{
	lines.clear();
	lines.push_back(std::make_pair(v2 - v1, v1));
	lines.push_back(std::make_pair(v3 - v2, v2));
	lines.push_back(std::make_pair(v4 - v3, v3));
	lines.push_back(std::make_pair(v1 - v4, v4));
}

void DotBox::applyMatrixTransformation(const Matrix22 & m)
{
	v1 = m * v1;
	v2 = m * v2;
	v3 = m * v3;
	v4 = m * v4;
	dot = m * dot;
}

void DotBox::applyMatrixTransformation(const Matrix22h & m)
{
	v1 = (m * Vector2h(v1)).asVector2();
	v2 = (m * Vector2h(v2)).asVector2();
	v3 = (m * Vector2h(v3)).asVector2();
	v4 = (m * Vector2h(v4)).asVector2();
	dot = (m * Vector2h(dot)).asVector2();
}