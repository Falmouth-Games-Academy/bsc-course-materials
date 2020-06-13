#include "stdafx.h"
#include "Application.h"
#include "Shape.h"
#include "Vector2h.h"

// Constructor -- initialise application-specific data here
Application::Application()
{
}

// Destructor -- delete any pointers/allocated memory
Application::~Application()
{
	for (auto s : m_shapes)
		if (s) delete s;
}

// Run the application
// Return true if the application finishes successfully, or false if an error occurs
bool Application::run()
{
	// Initialisation
	if (!initSDL())
		return false;
	
	// Add stuff
	addObjects();
	setColours();

	// Main loop
	m_quit = false;
	while (!m_quit)
	{
		// Process events
		SDL_Event ev;
		while (SDL_PollEvent(&ev))
		{
			processEvent(ev);
		}

		// Update objects
		update();

		// Render
		render();
		SDL_RenderPresent(m_renderer);
	}

	// Shutdown
	shutdownSDL();
	return true;
}

// Initialise the required parts of the SDL library
// Return true if initialisation is successful, or false if initialisation fails
bool Application::initSDL()
{
	if (SDL_Init(SDL_INIT_VIDEO) != 0)
	{
		std::cout << "SDL_Init Error: " << SDL_GetError() << std::endl;
		return false;
	}

	m_window = SDL_CreateWindow("COMP270", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, c_windowWidth, c_windowHeight, SDL_WINDOW_SHOWN);
	if (m_window == nullptr)
	{
		std::cout << "SDL_CreateWindow Error: " << SDL_GetError() << std::endl;
		return false;
	}

	m_renderer = SDL_CreateRenderer(m_window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
	if (m_renderer == nullptr)
	{
		std::cout << "SDL_CreateRenderer Error: " << SDL_GetError() << std::endl;
		return false;
	}

	return true;
}

// Shutdown the SDL library
void Application::shutdownSDL()
{
	if (m_renderer)
	{
		SDL_DestroyRenderer(m_renderer);
		m_renderer = nullptr;
	}

	if (m_window)
	{
		SDL_DestroyWindow(m_window);
		m_window = nullptr;
	}

	SDL_Quit();
}

// Process a single event
void Application::processEvent(const SDL_Event &ev)
{
	switch (ev.type)
	{
	case SDL_QUIT:
		m_quit = true;
		break;

	case SDL_KEYDOWN:
		if (ev.key.keysym.sym == SDLK_ESCAPE)
		{
			m_quit = true;
		}

		break;
	}
}

// Add objects to render
void Application::addObjects()
{
	// TO DO: use this space to carry out the exercises;
	// feel free to add your own objects!

	// Some initial objects
	Vector2 point(-7.0f, 5.0f);
	addPoint(point);

	Vector2 vec(1.5f, -3.7f), vec_start(2.0f, -1.0f);
	addVector(vec, vec_start);

	Vector2 dude_pos(3.0f, 2.0f);
	StickDude* dude = new StickDude(dude_pos);
	addShape(dude);

	Vector2 box1(-1.0f, 0.0f), box2(-1.0f, 3.0f), box3(1.0f, 3.0f), box4(1.0f, 0.0f), boxdot(0.5f, 2.5f);
	DotBox* box = new DotBox(box1, box2, box3, box4, boxdot);
	addShape(box);

	//-------------------------------------------------------------------------------------------------------------//

	// TO DO: Transform objects for Part B question 1
	// to apply matrix transformations
	Matrix22 m2a(0, 1, -1, 0);
	Vector2 trans_point = m2a * point, trans_vec = m2a * vec, trans_vec_start = m2a * vec_start;

	StickDude* trans_dude = new StickDude(dude_pos);
	trans_dude->applyMatrixTransformation(m2a);

	// Uncomment the following 3 lines to draw the transformed objects
	//addPoint(trans_point);
	//addVector(trans_vec, trans_vec_start);
	//addShape(trans_dude);

	//-------------------------------------------------------------------------------------------------------------//

	// TODO: Transform the DotBox for Part B question 2
	DotBox* trans_box = new DotBox(box1, box2, box3, box4, boxdot);

	// Uncomment the following line to draw the transformed box
	//addShape(trans_box);

	//-------------------------------------------------------------------------------------------------------------//

	// Setup for Part B, question 3a
	Vector2 p(-3.0f, 4.0f), v(5.0f, -2.0f);
	std::vector<Vector2> xes;
	xes.push_back(Vector2(0.0f, 0.0f));
	xes.push_back(Vector2(1.0f, 6.0f));
	xes.push_back(Vector2(-6.0f, 0.0f));
	xes.push_back(Vector2(-4.0f, 7.0f));
	xes.push_back(Vector2(5.0f, 5.0f));
	xes.push_back(Vector2(-3.0f, 0.0f));
	xes.push_back(Vector2(-6.0f, -3.5f));

	// Uncomment the following 6 lines to draw p and v
	// instead of the random objects:
	/*m_points.clear();
	m_vectors.clear();
	m_shapes.clear();
	addPoint(p);
	addVector(v, p);*/

	// Display all the x values:
	//m_points.insert(m_points.end(), xes.begin(), xes.end());

	// TO DO: add the code to find the relevant dot products/other values
	// and use them to display (add) only points that are:
	// a) visible to the NPC
	// b) invisible to the NPC
	for (const auto& x : xes)
	{
		bool visible = false;
		// ...

		if (visible)
		{
			// ...
		}
	}
}

void Application::setColours()
{
	m_colours.resize((m_points.size() + m_vectors.size() + m_shapes.size()) * 3);
	for (unsigned i = 0; i < m_colours.size(); ++i)
		m_colours[i] = 255 - rand() % 256;
}

// Called every time the main application loop runs
void Application::update()
{
	// TO DO: Add any time-varying updates to objects here
}

// Render the scene
void Application::render()
{
	SDL_SetRenderDrawColor(m_renderer, 0, 0, 0, 255);
	SDL_RenderClear(m_renderer);

	drawAxes();

	unsigned i = 0;
	for (auto p : m_points)
	{
		SDL_SetRenderDrawColor(m_renderer, m_colours[i++], m_colours[i++], m_colours[i++], 255);
		drawPoint(p);
	}
	for (auto v : m_vectors)
	{
		SDL_SetRenderDrawColor(m_renderer, m_colours[i++], m_colours[i++], m_colours[i++], 255);
		drawVector(v.first, v.second);
	}
	for (auto s : m_shapes)
	{
		SDL_SetRenderDrawColor(m_renderer, m_colours[i++], m_colours[i++], m_colours[i++], 255);
		drawShape(s);
	}
}

// Helper function to add a single point to the draw list
void Application::addPoint(const Vector2 & p)
{
	m_points.push_back(p);
}

// Helper function to add a vector to the draw list
void Application::addVector(const Vector2 & v, const Vector2 start)
{
	m_vectors.push_back(std::make_pair(v, start));
}

// Helper function to add a shape to the draw list
void Application::addShape(Shape * shape)
{
	m_shapes.push_back(shape);
}

// Draws a point in the correct place on the screen relative to the axes
void Application::drawPoint(const Vector2& p)
{
	Vector2 screen_pt = toScreenSpace(p);
	SDL_RenderDrawLineF(m_renderer, screen_pt.x - 2.5f, screen_pt.y - 2.5f, screen_pt.x + 2.5f, screen_pt.y + 2.5f);
	SDL_RenderDrawLineF(m_renderer, screen_pt.x - 2.5f, screen_pt.y + 2.5f, screen_pt.x + 2.5f, screen_pt.y - 2.5f);
}

// Draws a vector (a line with an arrow at the end) from the given start point
// in the correct place on the screen relative to the axes
// v: the vector (length/magnitude) to draw
// start: the position (x, y) relative to the origin to start drawing from
// withArrow: if true, an arrow will be drawn at the end of the vector to indicate direction
void Application::drawVector(const Vector2& v, const Vector2 start, bool withArrow)
{
	// Get the coordinates of the vector's end point
	Vector2 end = start + v;

	// Transform the points to screen space
	Vector2 start_screen = toScreenSpace(start), end_screen = toScreenSpace(end);

	// Draw the vector line
	SDL_RenderDrawLineF(m_renderer, start_screen.x, start_screen.y, end_screen.x, end_screen.y);

	if (withArrow)
	{
		// Draw the arrow at the end
		static const Vector2 arrow1(-0.2f, -0.2f), arrow2(-0.2f, 0.2f);
		float theta = atan2(v.y, v.x), cos_theta = cos(theta), sin_theta = sin(theta);
		Vector2 arrow1_rotated(arrow1.x * cos_theta - arrow1.y * sin_theta, arrow1.x * sin_theta + arrow1.y * cos_theta);
		Vector2 arrow2_rotated(arrow2.x * cos_theta - arrow2.y * sin_theta, arrow2.x * sin_theta + arrow2.y * cos_theta);

		Vector2 arrow1_screen = toScreenSpace(arrow1_rotated + end);
		Vector2 arrow2_screen = toScreenSpace(arrow2_rotated + end);
		SDL_RenderDrawLineF(m_renderer, end_screen.x, end_screen.y, arrow1_screen.x, arrow1_screen.y);
		SDL_RenderDrawLineF(m_renderer, end_screen.x, end_screen.y, arrow2_screen.x, arrow2_screen.y);
	}
}

// Draw a Shape object
void Application::drawShape(const Shape* shape)
{
	std::vector<Vector2> points;
	shape->getPoints(points);
	for (auto& p : points)
		drawPoint(p);

	std::vector<std::pair<Vector2, Vector2>> lines;
	shape->getLines(lines);
	for (auto& l : lines)
		drawVector(l.first, l.second, false);
}

// Draw the x and y axes
void Application::drawAxes()
{
	SDL_SetRenderDrawColor(m_renderer, 255, 255, 255, 255);
	drawVector(Vector2(c_max_x * 2.0f, 0.0), Vector2(-c_max_x, 0.0f));
	drawVector(Vector2(0.0f, c_max_y * 2.0f), Vector2(0.0f, -c_max_y));

	// Add scale markings
	Vector2 origin = toScreenSpace(Vector2(0.0f, 0.0f)), screen_scale = toScreenSpace(Vector2(1.0f, 1.0f)) - origin;
	float x = origin.x - screen_scale.x * c_max_x;
	while (x <= origin.x + screen_scale.x * c_max_x)
	{
		SDL_RenderDrawLineF(m_renderer, x, origin.y + 1.0f, x, origin.y - 1.0f);
		x += screen_scale.x;
	}
	float y = origin.y + screen_scale.y * c_max_y;
	while (y <= origin.y - screen_scale.y * c_max_y)
	{
		SDL_RenderDrawLineF(m_renderer, origin.x + 1.0f, y, origin.x - 1.0f, y);
		y -= screen_scale.y;
	}
}

Vector2 Application::toScreenSpace(const Vector2& v)
{
	// Find the centre point of the drawn window
	static const float screen_origin_x = float(c_windowWidth / 2);
	static const float screen_origin_y = float(c_windowHeight / 2);

	// Map the scale of the x and y coordinates to the size of the window
	static const float scale_x = (float(c_windowWidth) - 20.0f) / (c_max_x * 2.0f);
	static const float scale_y = -(float(c_windowHeight) - 20.0f) / (c_max_y * 2.0f);

	return Vector2(v.x * scale_x + screen_origin_x, v.y * scale_y + screen_origin_y);
}

// Application entry point
int main(int, char**)
{
	Application application;
	if (application.run())
		return 0;
	else
		return 1;
}
