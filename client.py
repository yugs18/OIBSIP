import socket
import threading

class ChatClient:
    def __init__(self, host='localhost', port=9999):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.nickname = input("Enter your nickname: ")

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == 'John':
                    self.client.send(self.nickname.encode('ascii'))
                else:
                    print(message)
            except:
                print("An error occurred!")
                self.client.close()
                break

    def write(self):
        while True:
            message = f'{self.nickname}: {input("")}'
            self.client.send(message.encode('ascii'))

if __name__ == '__main__':
    chat_client = ChatClient()
    receive_thread = threading.Thread(target=chat_client.receive)
    receive_thread.start()

    write_thread = threading.Thread(target=chat_client.write)
    write_thread.start()