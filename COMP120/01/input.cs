Console.WriteLine("Enter your name:");
name = Console.ReadLine();

Console.WriteLine("Enter your age:");
age = Int16.Parse(Console.ReadLine());

Console.WriteLine($"Hello {name}");
Console.WriteLine($"On your next birthday, you will be
{age+1} years old");
