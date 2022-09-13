int a = 0;
int b = 0;

for (int i = 0; i < 5; i++) 
{
	if (i < 3 || i > 7) 
	{
		a += i;
	} 
	else 
	{
		b += i;
	}
}
Console.WriteLine(a);
Console.WriteLine(b);
