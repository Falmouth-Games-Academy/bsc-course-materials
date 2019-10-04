using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

using Newtonsoft.Json;


namespace client
{
    class Entry
    {
        public Entry()
        {
        }

        public Entry(String name, int score)
        {
            this.name = name;
            this.score = score;
        }

        public String name;
        public int score;
    }

    class Program
    {
        static void Main(string[] args)
        {
            using (HttpClient client = new HttpClient())
            {
                client.BaseAddress = new Uri("http://localhost/");
                ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };


                try
                {                    
                    var response = client.GetAsync("player_data").Result;

                    if (response.IsSuccessStatusCode)
                    {
                        var responseContent = response.Content;

                        // by calling .Result you are synchronously reading the result
                        string responseString = responseContent.ReadAsStringAsync().Result;

                        var obj = JsonConvert.DeserializeObject<List<Entry>>(responseString);

                        foreach( var entry in obj)
                        {
                            Console.WriteLine(entry.name +" " + entry.score);
                        }
                    }

                }
                catch (HttpRequestException e)
                {
                    Console.WriteLine("\nException Caught!");
                    Console.WriteLine("Message :{0} ", e.Message);
                }

                try
                {
                    var new_score = new Entry("c# test", 999);

                    var content = new StringContent(JsonConvert.SerializeObject(new_score));

                    var response = client.PostAsync("add_score",content).Result;

                    if (response.IsSuccessStatusCode)
                    {
                        var responseContent = response.Content;

                        // by calling .Result you are synchronously reading the result
                        string responseString = responseContent.ReadAsStringAsync().Result;

                        var obj = JsonConvert.DeserializeObject<List<Entry>>(responseString);

                        Console.WriteLine(responseString);
                    }
                }
                catch (HttpRequestException e)
                {
                    Console.WriteLine(e.Message);
                    throw;
                }
            }
        }
    }
}
