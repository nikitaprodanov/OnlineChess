document.addEventListener('DOMContentLoaded', () => {
	var socket = io.connect('http://' + document.domain + ':' + location.port);

	socket.on('connect', () => {
		socket.send("I am connected");
	});

	socket.on('message', data => {
		const p = document.createElement('p');
		const br = document.createElement('br');
		p.innerHTML = data;
		document.querySelector('.display-message-section').append(p);
	});

	socket.on('some-event', data => {
		console.log(`${data}`);
	});

	document.querySelector('.send-message').onclick = () => {
		socket.send(document.querySelector('.user-message').value);
	}
})