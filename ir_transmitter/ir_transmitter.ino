#include <IRremote.h>

#define IR_SEND_PIN 32

IRsend sender;
uint16_t CurrentAddress = 0;
uint16_t CurrentCommand = 0;
String CurrentProtocol = "";
String input[2];

void parseInput( String str )
{
	int index = str.indexOf( ':' );
	int index2 = str.indexOf( ':', index + 1 );
	input[0] = str.substring( 0, index );
	input[1] = str.substring( index + 1, index2 );
}

void sendIR()
{
	CurrentProtocol.toLowerCase();
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
			CurrentProtocol = input[1];
		}
	}
}
