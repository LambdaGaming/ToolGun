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
	text.style.animation = `anim ${text.innerHTML.length / 4}s linear infinite` // Not perfect but works for now
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
	close()
}

function UpdateProgramList() {
	var list = document.getElementById( "programList" )
	eel.GetProgramList()( n => {
		for ( var i = 0; i < n.length; i++ ) ( function( i ) {
			var a = document.createElement( "a" )
			var textnode = document.createTextNode( n[i][0] )
			a.appendChild( textnode )
			a.addEventListener( "click", function() {
				eel.StartProgram( n[i][1] )
			} )
			list.appendChild( a )
		} )( i )
	} )
}

function UpdateExtraStat( num, info ) {
	var stat = document.getElementById( `extrastat${num}` )
	stat.innerText = info
	
}

function UpdateFunctionList() {
	var list = document.getElementById( "fileContainer" )
	eel.GetFunctionList()( n => {
		for ( var i = 0; i < n.length; i++ ) ( function( i ) {
			var a = document.createElement( "a" )
			var textnode = document.createTextNode( n[i] )
			a.appendChild( textnode )
			a.addEventListener( "click", function() {
				eel.ChangeFunction( i )
			} )
			list.appendChild( a )
		} ) ( i )
	} )
}
