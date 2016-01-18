#pragma once

struct Colour
{
	unsigned char r, g, b;
};

// Get a list of colours which give a rainbow effect
std::vector<Colour> getRainbow(int length);

