import zmq
import requests
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    if message == b"Requesting Data":
        api_url = "https://valorant-api.com/v1/agents"

        params = {
            "language":"en-US",
            "isPlayableCharacter": True
        }

        response = requests.get(api_url, params=params)
        
        if response.status_code == 200:
            data = response.json()

            agents = []
            for agent_data in data["data"]:
                agents.append(agent_data["displayName"])
                
            pseduo_random = random.randint(0, len(agents)-1)
            socket.send_string(agents[pseduo_random])
        
