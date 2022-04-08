function UpdateTime() {
	var date = new Date()
	var timeElement = document.getElementById( "time" )
	timeElement.innerHTML = date.getHours() + ":" + date.getMinutes()
}
