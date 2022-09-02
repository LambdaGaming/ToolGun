#include <ESPAsyncWebServer.h>
#include <ESPmDNS.h>
#include <IRremote.h>
#include <WiFi.h>

#define IR_SEND_PIN 32

IRsend sender;
const char *ssid = ""; // Wifi name
const char *password = ""; // Wifi password
AsyncWebServer server( 80 );
uint16_t CurrentAddress = 0;
uint16_t CurrentCommand = 0;
String CurrentProtocol = "";

void sendIR()
{
	if ( CurrentProtocol == "nec" ) {
  	sender.sendNEC( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "samsung" ) {
		sender.sendSamsung( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "samsung_lg" ) {
		sender.sendSamsungLG( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "sony" ) {
		sender.sendSony( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "panasonic" ) {
		sender.sendPanasonic( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "denon" ) {
		sender.sendDenon( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "sharp" ) {
		sender.sendSharp( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "lg" ) {
		sender.sendLG( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "jvc" ) {
		sender.sendJVC( ( uint8_t ) CurrentAddress, ( uint8_t ) CurrentCommand, 0 );
	} else if ( CurrentProtocol == "rc5" ) {
		sender.sendRC5( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "rc6" ) {
		sender.sendRC6( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "kaseikyo_jvc" ) {
		sender.sendKaseikyo_JVC( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "kaseikyo_denon" ) {
		sender.sendKaseikyo_Denon( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "kaseikyo_sharp" ) {
		sender.sendKaseikyo_Sharp( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "kaseikyo_mitsubishi" ) {
		sender.sendKaseikyo_Mitsubishi( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "onkyo" ) {
		sender.sendOnkyo( CurrentAddress, CurrentCommand, 0 );
	} else if ( CurrentProtocol == "apple" ) {
		sender.sendApple( CurrentAddress, CurrentCommand, 0 );
#ifndef EXCLUDE_EXOTIC_PROTOCOLS
	} else if ( CurrentProtocol == "bosewave" ) {
		sender.sendBoseWave( CurrentCommand, 0 );
	} else if ( CurrentProtocol == "lego_pf" ) {
		sender.sendLegoPowerFunctions( CurrentAddress, CurrentCommand, CurrentCommand >> 4 );
#endif
	}
}

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
    sendIR();
    request->send( 200, "text/plain", "OK" );
    digitalWrite( LED_BUILTIN, LOW );
  } );

  server.on( "/change", HTTP_POST, []( AsyncWebServerRequest *request ) {
    if ( request->hasParam( "address" ) )
      CurrentAddress = request->getParam( "address" )->value().toInt();
    if ( request->hasParam( "command" ) )
      CurrentCommand = request->getParam( "command" )->value().toInt();
    if ( request->hasParam( "protocol" ) )
      CurrentProtocol = request->getParam( "protocol" )->value();

    request->send( 200, "text/plain", "OK" );
  } );

  server.begin();
}

void loop() {}
