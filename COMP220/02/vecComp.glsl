vec4 a = vec4(1, 2, 3, 4);
float b = a.y; // b == 2
float c = a.z; // c == 3
a.x = 5;       // a == vec4(5, 2, 3, 4)
a.w = a.y;     // a == vec4(5, 2, 3, 2)