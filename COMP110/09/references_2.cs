class Foo
{
    public int value;

    public Foo(int v)
    {
        value = v;
    }
}

Foo a = new Foo(10);
Foo b = a;
a.value = 20;
Console.WriteLine($"a: {a.value}");
Console.WriteLine($"b: {b.value}");
