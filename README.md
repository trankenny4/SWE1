**Valorant Information Generator Command Line Interface Tool with Microservice**

Tool that generates Valorant information that can be viewed in the Command Line


Communication Contract:
  1) Import zmq with Python
  2) Connect to the microservice with the following lines:
           context = zmq.Context()
           socket = context.socket(zmq.REQ)
           socket.connect("tcp://localhost:5555")
           socket.send(b"Requesting Data")
  4) Data is received with the line:
           agent = socket.recv().decode()
