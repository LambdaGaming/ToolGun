#include <ESPAsyncWebServer.h>
#include <ESPmDNS.h>
#include <IRremote.h>
#include <WiFi.h>

#define IR_SEND_PIN 32

int triggerVal = 0;
IRsend sender;
const char *ssid = "";
const char *password = "";
AsyncWebServer server( 80 );
int CurrentAddress = 0;
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
  MDNS.begin( "toolgunremote" );
  pinMode( LED_BUILTIN, OUTPUT );

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
    digitalWrite( LED_BUILTIN, HIGH );
    sender.sendSamsung( CurrentAddress, CurrentCommand, 0 );
    request->send( 200, "text/plain", "OK" );
    digitalWrite( LED_BUILTIN, LOW );
  } );

  server.on( "/change", HTTP_POST, []( AsyncWebServerRequest *request ) {
    if ( request->hasParam( "address" ) && request->hasParam( "command" ) )
    {
      CurrentAddress = request->getParam( "address" )->value().toInt();
      CurrentCommand = request->getParam( "command" )->value().toInt();
    }
    request->send( 200, "text/plain", "OK" );
  } );

  server.begin();
}

void loop(){}
