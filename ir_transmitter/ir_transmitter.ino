#include <IRremote.h>

#define IR_SEND_PIN 32

IRsend sender;
uint16_t CurrentAddress = 0;
uint16_t CurrentCommand = 0;
decode_type_t CurrentProtocol = UNKNOWN;
String input[2];

void parseInput( String str )
{
	int index = str.indexOf( ':' );
	int index2 = str.indexOf( ':', index + 1 );
	input[0] = str.substring( 0, index );
	input[1] = str.substring( index + 1, index2 );
}

decode_type_t getProtocolFromString( String p )
{
	p.toLowerCase();
	if ( p == "nec" ) {
		CurrentProtocol = NEC;
	} else if ( p == "samsung" ) {
		CurrentProtocol = SAMSUNG;
	} else if ( p == "samsung_lg" ) {
		CurrentProtocol = SAMSUNG_LG;
	} else if ( p == "sony" ) {
		CurrentProtocol = SONY;
	} else if ( p == "panasonic" ) {
		CurrentProtocol = PANASONIC;
	} else if ( p == "denon" ) {
		CurrentProtocol = DENON;
	} else if ( p == "sharp" ) {
		CurrentProtocol = SHARP;
	} else if ( p == "lg" ) {
		CurrentProtocol = LG;
	} else if ( p == "jvc" ) {
		CurrentProtocol = JVC;
	} else if ( p == "rc5" ) {
		CurrentProtocol = RC5;
	} else if ( p == "rc6" ) {
		CurrentProtocol = RC6;
	} else if ( p == "kaseikyo_jvc" ) {
		CurrentProtocol = KASEIKYO_JVC;
	} else if ( p == "kaseikyo_denon" ) {
		CurrentProtocol = KASEIKYO_DENON;
	} else if ( p == "kaseikyo_sharp" ) {
		CurrentProtocol = KASEIKYO_SHARP;
	} else if ( p == "kaseikyo_mitsubishi" ) {
		CurrentProtocol = KASEIKYO_MITSUBISHI;
	} else if ( p == "onkyo" ) {
		CurrentProtocol = ONKYO;
	} else if ( p == "apple" ) {
		CurrentProtocol = APPLE;
#ifndef EXCLUDE_EXOTIC_PROTOCOLS
	} else if ( p == "bosewave" ) {
		CurrentProtocol = BOSEWAVE;
	} else if ( p == "lego_pf" ) {
		CurrentProtocol = LEGO_PF;
#endif
	}
}

void sendIR()
{
	IRData data;
	data.address = CurrentAddress;
	data.command = CurrentCommand;
	data.protocol = CurrentProtocol;
	sender.write( &data, 0 );
	Serial.println( "test" );
}

void setup()
{
	IrSender.begin( IR_SEND_PIN );
	Serial.begin( 115200 );
	pinMode( LED_BUILTIN, OUTPUT );
}

void loop()
{
  	if ( Serial.available() )
  	{
		parseInput( Serial.readString() );
		if ( input[0] == "fire" )
		{
	  		digitalWrite( LED_BUILTIN, HIGH );
			sendIR();
			digitalWrite( LED_BUILTIN, LOW );
		}
		else if ( input[0] == "address" )
		{
			CurrentAddress = input[1].toInt();
		}
		else if ( input[0] == "command" )
		{
			CurrentCommand = input[1].toInt();
		}
		else if ( input[0] == "protocol" )
		{
			CurrentProtocol = getProtocolFromString( input[1] );
		}
	}
}
