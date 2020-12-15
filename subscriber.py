import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB) # creating subscriber socket

configs = open('config.txt', 'r') # config file

ip = configs.readline().replace('\n', '') # host ip
port = configs.readline() # what port to use
p = 'tcp://' + ip + ':' + port # how to communicate

socket.connect(p) # connecting to the server
socket.setsockopt_string(zmq.SUBSCRIBE, 'Folder') # subscribing to 'Folder' messages

while True:
    content = socket.recv_string() # receive from publisher
    print(content)