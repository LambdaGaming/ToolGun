import requests

NAME = "Get Position"
DATA = []

def PullTrigger():
	ip = requests.get( "https://api64.ipify.org?format=json" ).json()["ip"]
	response = requests.get( f"https://ipapi.co/{ip}/json/" ).json()
	print( f"City: {response.get( 'city' )}" )
	print( f"Region: {response.get( 'region' )}" )
	print( f"Country: {response.get( 'country_name' )}" )
	print( f"Latitude: {response.get( 'latitude' )}" )
	print( f"Longitude: {response.get( 'longitude' )}" )

def ChangeData( index ):
	pass
