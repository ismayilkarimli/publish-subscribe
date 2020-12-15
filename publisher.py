import zmq, time, os
import subprocess as sp

dir = input('Enter directory: ')

context = zmq.Context()
socket = context.socket(zmq.PUB) # creating publisher socket

configs = open('config.txt', 'r') # config file

ip = configs.readline().replace('\n', '') # host ip
port = configs.readline() # what port to use
p = 'tcp://' + ip + ':' + port # how to communicate
socket.bind(p) # bind socket


contents = os.listdir(dir)

while True: # publisher will publish contents for 5 times
    for content in contents:
        socket.send_string('Folder ' + dir + ' has ' + content)
    time.sleep(2) # waiting 2 seconds before republishing contents of a directory