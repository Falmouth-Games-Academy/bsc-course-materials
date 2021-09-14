using System;
using System.Collections.Generic;

namespace TestProject
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            var personList = new Dictionary<string, int>
            {
                ["Alice"] = 23,
                ["Bob"] = 40,
                ["Charlie"] = 32
            };

            foreach (KeyValuePair<string, int> personDetails in personList)
			{
                Console.WriteLine($"{personDetails.Key} is {personDetails.Value} years old");
			}

            Console.ReadKey();
        }
    }
}
