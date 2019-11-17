using System;

namespace TestProject
{
    class Pair<ElementType>
    {
        public ElementType first;
        public ElementType second;

        public Pair(ElementType f, ElementType s)
        {
            first = f;
            second = s;
        }
    }

    class MainClass
    {
        public static void Main(string[] args)
        {
            var p = new Pair<string>("hello", "world");
            Console.WriteLine("{0}, {1}", p.first, p.second);
        }
    }
}
