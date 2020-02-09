#version 330 core

layout(location = 0) in vec3 vertexPos;

void main()
{
    gl_Position.xyz = vec4(vertexPos,1.0);
}