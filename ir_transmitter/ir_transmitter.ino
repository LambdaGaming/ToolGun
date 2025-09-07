#include <ESPAsyncWebServer.h>
#include <ESPmDNS.h>
#include <IRremote.h>
#include <WiFi.h>

#define IR_SEND_PIN 32
#define DISABLE_CODE_FOR_RECEIVER

IRsend sender;
const char *ssid = ""; // Wifi name
const char *password = ""; // Wifi password
AsyncWebServer server( 80 );
int_fast8_t repeats = 0;
IRData data;

// Protocol names can be found at https://github.com/Arduino-IRremote/Arduino-IRremote/blob/master/src/IRProtocol.hpp
decode_type_t getProtocolFromString( const char* str )
{
	decode_type_t proto = UNKNOWN;
	uint8_t i = 0;
	while( i != OTHER )
	{
		if ( ProtocolNames[i] == str )
		{
			proto = ( decode_type_t ) i;
			break;
		}
		i++;
	}
	return proto;
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
		sender.write( &data, repeats );
		request->send( 200, "text/plain", "OK" );
		digitalWrite( LED_BUILTIN, LOW );
	} );

	server.on( "/change", HTTP_POST, []( AsyncWebServerRequest *request ) {
		if ( !request->hasParam( "address" ) || !request->hasParam( "command" ) || !request->hasParam( "protocol" ) )
		{
			request->send( 400, "text/plain", "Bad Request" );
			return;
		}
		if ( request->hasParam( "repeats" ) )
		{
			repeats = request->getParam( "repeats" )->value().toInt();
		}
		data.address = request->getParam( "address" )->value().toInt();
		data.command = request->getParam( "command" )->value().toInt();
		data.flags = IRDATA_FLAGS_EMPTY;
		data.protocol = getProtocolFromString( request->getParam( "protocol" )->value().c_str() );
		request->send( 200, "text/plain", "OK" );
	} );

	server.begin();
}

void loop() {}
