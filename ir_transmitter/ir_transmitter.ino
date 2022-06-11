#include <ESPAsyncWebServer.h>
#include <IRremote.h>
#include <WiFi.h>

#define IR_SEND_PIN 32

int triggerVal = 0;
IRsend sender;
const char *ssid = "MLJM-24";
const char *password = "1504928e74";
AsyncWebServer server( 80 );
int CurrentCommand = 0;

void setup()
{
  IrSender.begin( IR_SEND_PIN );
  Serial.begin( 115200 );
  delay( 10 );
  Serial.println();
  Serial.print( "Connecting to "  );
  Serial.println( ssid );
  WiFi.begin( ssid, password );

  while ( WiFi.status() != WL_CONNECTED )
  {
    delay( 500 );
    Serial.print( "." );
  }

  Serial.println();
  Serial.println( "WiFi connected." );
  Serial.print( "IP address: " );
  Serial.println( WiFi.localIP() );

  server.on( "/fire", HTTP_POST, []( AsyncWebServerRequest *request ) {
    sender.sendSamsung( 0x707, CurrentCommand, 0 );
    request->send( 200, "text/plain", "OK" );
  } );

  server.on( "/change", HTTP_POST, []( AsyncWebServerRequest *request ) {
    if ( request->hasParam( "command" ) )
    {
      CurrentCommand = request->getParam( "command" )->value().toInt();
    }
    request->send( 200, "text/plain", "OK" );
  } );

  server.begin();
}

void loop(){}
