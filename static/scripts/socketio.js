document.addEventListener('DOMContentLoaded', () => {
	var socket = io.connect('http://' + document.domain + ':' + location.port);

	socket.on('connect', () => {
		socket.send("I am connected");
	});

	socket.on('message', data => {
		const p = document.createElement('p');
		const span_username = document.createElement('span');
		const br = document.createElement('br');
		span_username.innerHTML = data.username;
		p.innerHTML = span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML;
		document.querySelector('.display-message-section').append(p);
	});

	socket.on('some-event', data => {
		console.log(`${data}`);
	});

	document.querySelector('.send-message').onclick = () => {
		socket.send({'msg': document.querySelector('.user-message').value, 'username': username});
	}
})