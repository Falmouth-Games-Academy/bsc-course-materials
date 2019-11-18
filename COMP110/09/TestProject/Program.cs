using System;
using System.Collections.Generic;

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

    struct Foo
    {
        public string a;
        public int b;
    }

    class MainClass
    {
        public static void Main(string[] args)
        {
            var q = new int[,] { { 1, 2, 3 }, { 4, 5, 6 } };

            var p = new Pair<string>("hello", "world");
            Console.WriteLine("{0}, {1}", p.first, p.second);

            int[,,,,] a = new int[10, 10, 10, 10, 10];

            Console.WriteLine("{0}", a);

            var myList = new List<int>();

            string s = "Hello";
            s += "world";

            Dictionary<List<int>, string> d = new Dictionary<List<int>, string>();

            var age = new Dictionary<string, int>
            {
                ["Alice"] = 23,
                ["Bob"] = 36,
                ["Charlie"] = 27
            };

            Console.WriteLine(age["Alice"]);  // prints 23
            age["Bob"] = 40;     // overwriting an existing item
            age.Add("Emily", 29);
            age["Denise"] = 21;  // adding a new item      

            foreach (var kv in age)
            {
                Console.WriteLine("{0} is {1} years old", kv.Key, kv.Value);
            }

            Dictionary<int, int> sqrt = new Dictionary<int, int>();
            for (int i = 0; i < 30; i++)
                sqrt[i * i] = i;

            foreach (var kv in sqrt)
                Console.WriteLine("{0} {1}", kv.Key, kv.Value);
        }
    }
}
