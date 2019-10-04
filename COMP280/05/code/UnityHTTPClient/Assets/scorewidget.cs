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


public static class JsonHelper
{
    public static T[] FromJson<T>(string json)
    {
        Wrapper<T> wrapper = JsonUtility.FromJson<Wrapper<T>>(json);
        return wrapper.Items;
    }

    public static string ToJson<T>(T[] array)
    {
        Wrapper<T> wrapper = new Wrapper<T>();
        wrapper.Items = array;
        return JsonUtility.ToJson(wrapper);
    }

    public static string ToJson<T>(T[] array, bool prettyPrint)
    {
        Wrapper<T> wrapper = new Wrapper<T>();
        wrapper.Items = array;
        return JsonUtility.ToJson(wrapper, prettyPrint);
    }

    [Serializable]
    private class Wrapper<T>
    {
        public T[] Items;
    }


    public static string fixJson(string value)
    {
        value = "{\"Items\":" + value + "}";
        return value;
    }

}

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

                    var obj = JsonConvert.DeserializeObject<List<HiScoreEntry>>(responseString);

                    String text = "";

                    foreach (var entry in obj)
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
