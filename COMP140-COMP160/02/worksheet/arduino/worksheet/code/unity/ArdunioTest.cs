using UnityEngine;
//Using statements for Serial Port
using System.IO.Ports;
using System.Collections;
//System is also needed
using System;

public class ArdunioTest : MonoBehaviour
{
    //Public string for changing the port, we could enumrate and the Ports
    //but this is fine for an example
    public string COMPort = "COM4";

    //Serial Port, this will hold the instance of the serial Port
    //This is the main way to communicate with the serial device
    SerialPort serialPort;


    // Use this for initialization
    void Start()
    {
        //Initialise the serial port
        serialPort = new SerialPort();
        //Using the following port
        serialPort.PortName = COMPort;
        //Parity bits, this is used for error checking and must be agreed on by the device
        //and the host. In this case we don't use it!
        serialPort.Parity = Parity.None;
        //The Baud Rate is set to 9600, this is the default for mostn serial coms
        serialPort.BaudRate = 9600;
        //This is the length of bits communicated between the devices, the default is 8
        serialPort.DataBits = 8;
        //The stop bits in the data, per byte
        serialPort.StopBits = StopBits.One;

        //Open the port
        serialPort.Open();

    }

    // Update is called once per frame
    void Update()
    {
        //Read the data from the serial port, this will bring it back as a string.
        //There are a whole bunch of read functions, see the following for more info
        //https://msdn.microsoft.com/en-us/library/system.io.ports.serialport.readline(v=vs.110).aspx
        string data = serialPort.ReadLine();

        //You should now be able to cast the data as anything you want!

        //Simple log statement
        Debug.Log("Data from Arduino " + data);
    }

    //This called when the application quits (in editor and in standalone)
    void OnApplicationQuit()
    {
        //We must close the serial port
        serialPort.Close();
    }
}