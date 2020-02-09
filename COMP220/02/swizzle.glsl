vec4 a = vec4(1, 2, 3, 4);
vec2 b = a.xy;    // b == vec2(1, 2)
vec3 c = a.zyz;   // c == vec3(3, 2, 3)
a.xw = vec2(5,6); // a == vec4(5, 2, 3, 6)
a.xyzw = a.wzyx;  // a == vec4(6, 3, 2, 5)