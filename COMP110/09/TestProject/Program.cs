using System;
using System.Collections.Generic;

namespace TestProject
{
    class MainClass
    {
        public static bool approxEqual(double x, double y)
        {
            double diff = Math.Abs(x - y);
            return diff < 1e-5;
        }

        public static void Main(string[] args)
        {
            decimal a = 0.1m;
            decimal b = 0.2m;
            decimal c = 0.3m;

            if (a + b == c)
                Console.WriteLine("The world makes sense");
            else
                Console.WriteLine("The world makes NO sense :(");


            Console.WriteLine("{0:G9}", a + b - c);
        }
    }
}
