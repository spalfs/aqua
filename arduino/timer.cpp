#include <Arduino.h>

void wait(unsigned long t){
    unsigned long start = millis();
    while(millis()-start < t);
}

void setup(){
    pinMode(13,OUTPUT);
}

void loop(){
    digitalWrite(13,LOW);
    wait(30*1000);
    wait(30*1000);
    digitalWrite(13,HIGH);
    wait(30*1000);
    wait(30*1000);
}
