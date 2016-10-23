#include <Arduino.h>
#include <SoftwareSerial.h>

// pH Sensor Initalization
SoftwareSerial phSerial(2,3);
String pH = "";
bool phComplete = false;

// Pin Initialization
void setup(){
    Serial.begin(9600);
    phSerial.begin(9600);
    pH.reserve(30);
}

// Data RX/TX
void loop(){
    // Wait for go ahead 
    while(true){
        if(Serial.readString()!="")
            break;
        delay(500);
    }

    // Collect Data
    if(phSerial.available()){
        char in = (char)phSerial.read();
        pH += in;
        if(in == '\r'){
            phComplete = true;
        }
    }

    // Format Data
    String data;
    
    data = "55,";
    
    if(phComplete)
        data += pH;
    else
        data += "0,";
    
    data += "20,";
    
    data += String(10) + ",";
    
    // Send data Serially
    if (Serial)
        Serial.println(data);
}
