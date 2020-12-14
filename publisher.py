import zmq, time, os, csv

dir = input('Enter directory: ')

context = zmq.Context()
socket = context.socket(zmq.PUB) # creating publisher socket

file = open('config.csv', 'r') # config file
reader = csv.reader(file)
configs = [(ip, port) for row, (ip, port) in enumerate(reader) if row == 1]

ip = configs[0][0] # host ip
port = configs[0][1] # what port to use
p = 'tcp://' + ip + ':' + port # how to communicate
socket.bind(p) # bind socket

while True:
    contents = os.listdir(dir) # gathering directory contents

    for content in contents:
        socket.send_string('Folder ' + dir + ' has ' + content)
    time.sleep(10) # waiting 10 seconds before republishing contents of a directory
