#include <IRremote.h>

IRsend sender;

void setup() {
  
}

void loop() {
  sender.setSendPin( 19 );
  uint32_t dat = 0xEF10FF00;
  uint8_t len = 32;
  sender.sendNEC( dat, len );
  delay( 500 );
}
