class Thing
{
    public int a, b;

    public Thing(int a_, int b_)
    {
        a = a_; b = b_;
    }
}

Thing x = new Thing(30, 40);
Thing y = new Thing(50, 60);
Thing z = y;
