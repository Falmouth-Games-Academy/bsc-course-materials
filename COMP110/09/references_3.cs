class Foo
{
    public int value;

    public Foo(int v)
    {
        value = v;
    }
}

Foo a = new Foo(10);
Foo b = new Foo(10);
a.value = 20;
Console.WriteLine($"a: {a.value}");
Console.WriteLine($"b: {b.value}");
