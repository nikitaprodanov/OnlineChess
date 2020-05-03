document.addEventListener('DOMContentLoaded', () => {
	var socket = io.connect('http://' + document.domain + ':' + location.port);
	
	let room = "Lobby";
	joinRoom("Lobby");

	socket.on('connect', () => {
		socket.send("I am connected");
	});

	// Display messages
	socket.on('message', data => {
		const p = document.createElement('p');
		const span_username = document.createElement('span');
		const span_timestamp = document.createElement('span');
		const br = document.createElement('br');

		if (data.username) {
			span_username.innerHTML = data.username;
			span_timestamp.innerHTML = data.time_stamp;
			p.innerHTML = span_username.outerHTML + br.outerHTML;
			p.innerHTML += data.msg;
			p.innerHTML += br.outerHTML + span_timestamp.outerHTML;
			document.querySelector('.display-message-section').append(p);
		}
		else {
			printSysMsg(data.msg);
		}
	});

	socket.on('clear-message', data => {
		document.querySelector('.display-message-section').innerHTML = '';
	});

	// Send messages
	document.querySelector('.send-message').onclick = () => {
		socket.send({'msg': document.querySelector('.user-message').value, 'username': username, 'room': room });
	}

	// Room navigation
	document.querySelectorAll('.select-room').forEach(p => {
		p.onclick = () => {
			let newRoom = p.innerHTML;
			if (newRoom == room) {
				msg = `You are already in ${room} room.`
				printSysMsg(msg);
			}
			else {
				leaveRoom(room);
				joinRoom(newRoom);
				room = newRoom;
			}
		}
	});


	// Leave the room
	function leaveRoom(room) {
		socket.emit('leave', {'username': username, 'room': room});
	}

	// Join the room
	function joinRoom(room) {
		socket.emit('join', {'username': username, 'room': room});

		// Clear the message area
		document.querySelector('.display-message-section').innerHTML = '';
	}

	// Print system messages
	function printSysMsg(msg) {
		const p = document.createElement('p');
		p.innerHTML = msg;
		document.querySelector('.display-message-section').append(p);
	}

})