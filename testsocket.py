
import socketio

sio = socketio.Client()


@sio.on('connect')
def connect():
	print('Connected')

@sio.on('test')
def test():
	print('Test')

if __name__ == '__main__':
	sio.connect('http://192.168.43.135:5000')
