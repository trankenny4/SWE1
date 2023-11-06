**Valorant Information Generator Command Line Interface Tool with Microservice**

Tool that generates Valorant information that can be viewed in the Command Line


Communication Contract:
  1) Import zmq with Python
  2) Connect to the microservice with the following lines: <br />
           context = zmq.Context() <br />
           socket = context.socket(zmq.REQ) <br />
           socket.connect("tcp://localhost:5555") <br />
           socket.send(b"Requesting Data") <br />
  4) Data is received with the line: <br />
           agent = socket.recv().decode() <br />
