import zmq, csv

context = zmq.Context()
socket = context.socket(zmq.SUB) # creating subscriber socket

file = open('config.csv', 'r') # config file
reader = csv.reader(file)
configs = [(ip, port) for row, (ip, port) in enumerate(reader) if row == 1]

ip = configs[0][0] # host ip
port = configs[0][1] # what port to use
p = 'tcp://' + ip + ':' + port # how to communicate

socket.connect(p) # connecting to the server
socket.setsockopt_string(zmq.SUBSCRIBE, 'Folder') # subscribing to 'Folder' messages


while True:
    content = socket.recv_string() # receive from publisher
    print(content)