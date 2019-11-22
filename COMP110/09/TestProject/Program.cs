using System;
using System.Collections.Generic;

namespace TestProject
{
    class PairOfInts
    {
        public int first;
        public int second;

        public PairOfInts(int a, int b)
        {
            first = a;
            second = b;
        }
    }

    class PairOfStrings
    {
        public string first;
        public string second;

        public PairOfStrings(string a, string b)
        {
            first = a;
            second = b;
        }
    }

    class PairOfObjects
    {
        public object first;
        public object second;

        public PairOfObjects(object a, object b)
        {
            first = a;
            second = b;
        }
    }

    class Pair<ElementType>
    {
        public ElementType first;
        public ElementType second;

        public Pair(ElementType a, ElementType b)
        {
            first = a;
            second = b;
        }
    }



    class MainClass
    {
        public static void Main(string[] args)
        {
            var mySet = new HashSet<int> { 12, 34, 56 };
            mySet.Add(564);
            mySet.Add(12);

            foreach (int x in mySet)
                Console.WriteLine(x);
        }
    }
}
