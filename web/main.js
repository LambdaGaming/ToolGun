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
	text.innerHTML = sessionStorage.getItem( "CurrentTitle" ) || "ToolGun"
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

function UpdateCurrentData() {
	var text = document.getElementById( "currentData" )
	text.innerHTML = sessionStorage.getItem( "CurrentData" ) || "None"
}

function ToggleMute() {
	eel.ToggleMute()
	UpdateVolume()
}

function UpdateToolList() {
	var list = document.getElementById( "toolList" )
	eel.GetToolList()( n => {
		for ( var i = 0; i < n.length; i++ ) ( function( i ) {
			var a = document.createElement( "a" )
			var textnode = document.createTextNode( n[i][0] )
			a.appendChild( textnode )
			a.addEventListener( "click", function() {
				eel.ChangeTool( n[i][1] )
				sessionStorage.setItem( "CurrentTitle", n[i][0] )
				sessionStorage.removeItem( "CurrentData" )
				location.href = "main.html"
			} )
			list.appendChild( a )
		} )( i )
	} )
}

function UpdateDataList() {
	var list = document.getElementById( "fileContainer" )
	eel.GetDataList()( n => {
		for ( var i = 0; i < n.length; i++ ) ( function( i ) {
			var a = document.createElement( "a" )
			var textnode = document.createTextNode( n[i] )
			a.appendChild( textnode )
			a.addEventListener( "click", function() {
				eel.ChangeData( i )
				sessionStorage.setItem( "CurrentData", n[i] )
				location.href = "main.html"
			} )
			list.appendChild( a )
		} ) ( i )
	} )
}
