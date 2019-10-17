using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using System.Net;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;


class HiScoreEntry
{
    public HiScoreEntry()
    {
    }

    public HiScoreEntry(String name, int score)
    {
        this.name = name;
        this.score = score;
    }

    public String name;
    public int score;
}

class HiScoreEntries
{
    public HiScoreEntries()
    {

    }

    public List<HiScoreEntry> details;
}


public class scorewidget : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        GetScores();
    }

    public void GetScores()
    {
        using (HttpClient client = new HttpClient())
        {
            client.BaseAddress = new Uri("http://localhost:8000/");
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

            try
            {
                var response = client.GetAsync("player_data").Result;

                if (response.IsSuccessStatusCode)
                {
                    var responseContent = response.Content;

                    // by calling .Result you are synchronously reading the result
                    string responseString = responseContent.ReadAsStringAsync().Result;

                    var obj = JsonConvert.DeserializeObject<HiScoreEntries>(responseString);

                    String text = "";

                    foreach (var entry in obj.details)
                    {
                        text += entry.name + " " + entry.score;
                        text += "\n";
                    }

                    transform.Find("score_text").GetComponent<UnityEngine.UI.Text>().text = text;
                }
            }
            //catch (HttpRequestException e)
            catch (Exception e)
            {
                Debug.LogWarning("\nException Caught!");
                Debug.LogWarning(e.Message);
            }
        }
    }

    public void AddScore()
    {
        using (HttpClient client = new HttpClient())
        {
            client.BaseAddress = new Uri("http://localhost:8000/");
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

            try
            {
                var new_name = transform.Find("score_name").transform.Find("Text").GetComponent<UnityEngine.UI.Text>().text;
                var new_score = transform.Find("score_value").transform.Find("Text").GetComponent<UnityEngine.UI.Text>().text;


                var new_entry = new HiScoreEntry(new_name, Int32.Parse(new_score));

                var content = new StringContent(JsonConvert.SerializeObject(new_entry));

                var response = client.PostAsync("add_score", content).Result;

                if (response.IsSuccessStatusCode)
                {
                    var responseContent = response.Content;

                    // by calling .Result you are synchronously reading the result
                    string responseString = responseContent.ReadAsStringAsync().Result;

                    Console.WriteLine(responseString);
                }

                GetScores();
            }
            catch (Exception e)
            {
                Debug.LogWarning("\nException Caught!");
                Debug.LogWarning(e.Message);
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
