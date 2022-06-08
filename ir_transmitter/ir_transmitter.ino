#include <IRremote.h>

#define IR_SEND_PIN 32

IRsend sender;

void setup() {
  IrSender.begin( IR_SEND_PIN );
}

void loop() {
  
  sender.sendSamsung( 0x707, 0x2, 0 );
  delay( 1000 );
}
