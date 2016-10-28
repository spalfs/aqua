#include <Arduino.h>
#include <SoftwareSerial.h>
#include <DHT22.h>
#include <OneWire.h>

// pH Sensor 
//SoftwareSerial phSerial(2,3);
//String pH = "";
//bool phComplete = false;

// DHT 22
DHT22 dht(2);

// TMP 
OneWire ds(3);

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

  byte i;
  byte present = 0;
  byte type_s;
  byte adata[12];
  byte addr[8];
  float celsius, fahrenheit;

  if ( !ds.search(addr)) {
    Serial.println("No more addresses.");
    Serial.println();
    ds.reset_search();
    delay(250);
    return;
  }
  if (OneWire::crc8(addr, 7) != addr[7]) {
      Serial.println("CRC is not valid!");
      return;
  }
  /*
  switch (addr[0]) {
    case 0x10:
      Serial.println("  Chip = DS18S20");  // or old DS1820
      type_s = 1;
      break;
    case 0x28:
      Serial.println("  Chip = DS18B20");
      type_s = 0;
      break;
    case 0x22:
      Serial.println("  Chip = DS1822");
      type_s = 0;
      break;
    default:
      Serial.println("Device is not a DS18x20 family device.");
      return;
  } 
  */
  type_s = 0;
  ds.reset();
  ds.select(addr);
  ds.write(0x44, 1);        // start conversion, with parasite power on at the end
  
  delay(1000);     // maybe 750ms is enough, maybe not
  // we might do a ds.depower() here, but the reset will take care of it.
  
  present = ds.reset();
  ds.select(addr);    
  ds.write(0xBE);         // Read Scratchpad

  Serial.print("  Data = ");
  Serial.print(present, HEX);
  Serial.print(" ");
  for ( i = 0; i < 9; i++) {           // we need 9 bytes
    adata[i] = ds.read();
    Serial.print(adata[i], HEX);
    Serial.print(" ");
  }
  Serial.print(" CRC=");
  Serial.print(OneWire::crc8(adata, 8), HEX);
  Serial.println();

  // Convert the data to actual temperature
  // because the result is a 16 bit signed integer, it should
  // be stored to an "int16_t" type, which is always 16 bits
  // even when compiled on a 32 bit processor.
  int16_t raw = (adata[1] << 8) | adata[0];
  if (type_s) {
    raw = raw << 3; // 9 bit resolution default
    if (adata[7] == 0x10) {
      // "count remain" gives full 12 bit resolution
      raw = (raw & 0xFFF0) + 12 - adata[6];
    }
  } else {
    byte cfg = (adata[4] & 0x60);
    // at lower res, the low bits are undefined, so let's zero them
    if (cfg == 0x00) raw = raw & ~7;  // 9 bit resolution, 93.75 ms
    else if (cfg == 0x20) raw = raw & ~3; // 10 bit res, 187.5 ms
    else if (cfg == 0x40) raw = raw & ~1; // 11 bit res, 375 ms
    //// default is 12 bit resolution, 750 ms conversion time
  }
  celsius = (float)raw / 16.0;
  fahrenheit = celsius * 1.8 + 32.0;



    // Format Data
    String data;
    
    data =  "RTmp:";
    data += String(dht.getTemperatureF()) + "\n"; 
    
    data += "Humi:";
    data += String(dht.getHumidity()) + "\n";

    data += "WTmp:";
    data += String(fahrenheit) + "\n";
    
    /*
    if(phComplete)
        data += pH;
    else
        data += "0,";
    */ 
    
    // Send data Serially
    if (Serial)
        Serial.println(data);
    
    delay(1000);
}
