function UpdateTime() {
	var date = new Date()
	var timeElement = document.getElementById( "time" )
	timeElement.innerHTML = date.toLocaleString( "en-US", { hour: "numeric", minute: "numeric", hour12: false } )
}

function UpdateVolume() {
	var speaker = document.getElementById( "speaker" )
	eel.IsMuted()( n => {
		if ( n ) {
			speaker.src = "images/speaker_off.png"
		}
		else {
			speaker.src = "images/speaker_on.png"
		}
	} )
}
