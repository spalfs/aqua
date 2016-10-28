#include <Arduino.h>
#include <SoftwareSerial.h>
#include <DHT22.h>
#include <OneWire.h>

// Globals
int i;

// pH Sensor 
//SoftwareSerial phSerial(2,3);
//String pH = "";
//bool phComplete = false;

// DHT 22
DHT22 dht(2);

// TMP 
OneWire ds(3);
bool found = false;
byte adata[12];
byte addr[8];
float waterTemp;

float getWaterTemp(){
    if(!found){
        if (!ds.search(addr)){
            ds.reset_search();
            return 0;
        }
        else
            found = true;
    }
  
    ds.reset();
    ds.select(addr);
    ds.write(0x44, 1); 
  
    delay(1000); 

    ds.reset();
    ds.select(addr);    
    ds.write(0xBE); 
    for ( i = 0; i < 9; i++) adata[i] = ds.read();
    int16_t raw = (adata[1] << 8) | adata[0];
    return ((float)raw / 16.0) * 1.8 + 32.0;
}

// Pin Initialization
void setup(){
    Serial.begin(9600);
    //phSerial.begin(9600);
    //pH.reserve(30);
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
    /*
    if(phSerial.available()){
        char in = (char)phSerial.read();
        pH += in;
        if(in == '\r'){
            phComplete = true;
        }
    }
    */

    dht.readData();
    waterTemp = getWaterTemp();

    // Format Data
    String data;
    
    data =  "RTmp:";
    data += String(dht.getTemperatureF()) + "\n"; 
    
    data += "Humi:";
    data += String(dht.getHumidity()) + "\n";

    data += "WTmp:";
    data += String(waterTemp) + "\n";
    
    /*
    if(phComplete)
        data += pH;
    else
        data += "0,";
    */ 
    
    // Send data Serially
    if (Serial)
        Serial.println(data);
    
    delay(2000);
}
