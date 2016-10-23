#include <Arduino.h>

void setup(){
    Serial.begin(9600);
}

void loop(){
    // Wait for go ahead 
    while(true){
        if(Serial.readString()!="")
            break;
        delay(500);
    }
    // Collect Data
    String data;
    data = "55,";
    data += "20,";
    data += String(10) + ",";
    
    // Send data Serially
    if (Serial)
        Serial.println(data);
}
