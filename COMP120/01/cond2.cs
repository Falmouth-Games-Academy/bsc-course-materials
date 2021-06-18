int a = Int16.Parse(Console
.ReadLine());

int b = 0;

if (a < 20){
	b = a + 1;
} else if (a == 20) {
	b = a * 2;
} else {
	a = 20;
	b = 20;
}

Console.WriteLine(a);
Console.WriteLine(b);
