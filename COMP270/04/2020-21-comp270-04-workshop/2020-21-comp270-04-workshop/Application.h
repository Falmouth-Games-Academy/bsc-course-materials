#pragma once
#include "Vector2.h"

class Shape;

class Application
{
public:
	Application();
	~Application();

	bool run();

private:
	bool initSDL();
	void shutdownSDL();

	void processEvent(const SDL_Event &e);
	void addObjects();
	void setColours();
	void update();
	void render();

	void addPoint(const Vector2& p);
	void addVector(const Vector2& v, const Vector2 start = Vector2(0.0f, 0.0f));
	void addShape(Shape* shape);

	void drawPoint(const Vector2& p);
	void drawVector(const Vector2& v, const Vector2 start = Vector2(0.0f, 0.0f), bool withArrow = true);
	void drawShape(const Shape* shape);
	void drawAxes();

	Vector2 toScreenSpace(const Vector2& v);

	const int c_windowWidth = 700;
	const int c_windowHeight = 700;
	const float c_max_x = 12;
	const float c_max_y = 12;

	SDL_Window *m_window = nullptr;
	SDL_Renderer *m_renderer = nullptr;

	bool m_quit = false;

	// m_points is an array of Vector2 values representing x,y positions to draw as separate points
	std::vector<Vector2> m_points;

	// m_vectors is an array of pairs of Vector2 values describing how to draw vectors;
	// the first item in the pair is the vector itself and the second is the x,y position
	// to start drawing from.
	std::vector<std::pair<Vector2, Vector2>> m_vectors;

	// m_shapes is an array of Shape objects (see Shape.h)
	std::vector<Shape*> m_shapes;

	// The application assigns each object (point, vector or shape) a
	// random colour, which is stored in m_colours.
	std::vector<int> m_colours;
};
