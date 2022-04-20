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

function UpdateScrollText() {
	var text = document.getElementById( "contentTitle" )
	text.style.animation = "anim " + text.innerHTML.length / 4 + "s linear infinite" // Not perfect but works for now
}

function UpdatePerformanceStats() {
	var cpustats = document.getElementById( "cpustats" )
	var gpustats = document.getElementById( "gpustats" )
	var ramstats = document.getElementById( "ramstats" )

	eel.GetPerformanceStats()( n => {
		cpustats.innerHTML = `${n[0]}%`
		gpustats.innerHTML = `${n[1]}c`
		ramstats.innerHTML = `${n[2]}%`
	} )
}

function ToggleMute() {
	eel.ToggleMute()
	UpdateVolume()
}

function Shutdown() {
	eel.Shutdown()
	window.close()
}
