#include "stdafx.h"
#include "colours.h"

std::vector<Colour> getRainbow(int length)
{
	// Initialise the result vector
	std::vector<Colour> result;
	result.resize(length);

	for (int i = 0; i < length; i++)
	{
		// The following is based on the algorithm for converting HSV to RGB
		// https://en.wikipedia.org/wiki/HSL_and_HSV#Converting_to_RGB
		// Here we have fixed S=1 and V=1

		Colour& colour = result[i];
		double hue = 6 * (double)i / (double)length;
		double dx = 1.0 - abs(fmod(hue, 2.0) - 1.0);
		unsigned char x = (unsigned char)(dx * 255.0);
		unsigned char c = 255;

		switch ((int)hue)
		{
		case 0: colour = { c, x, 0 }; break;
		case 1: colour = { x, c, 0 }; break;
		case 2: colour = { 0, c, x }; break;
		case 3: colour = { 0, x, c }; break;
		case 4: colour = { x, 0, c }; break;
		case 5: colour = { c, 0, x }; break;
		default: throw std::exception("Invalid hue value");
		}
	}

	return result;
}
