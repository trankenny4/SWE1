from clint.textui import puts, colored, indent
from InquirerPy import inquirer
from InquirerPy.utils import color_print


import requests

api_url = "https://valorant-api.com/v1/agents"

params = {
    "language":"en-US",
    "isPlayableCharacter": True
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()
else:
    print("Failed to retrieve data. Status code:", response.status_code)

####################################################################################

banner = """
_  _ ____ _    ____ ____ ____ _  _ ___    _ _  _ ____ ____    ____ ____ _  _ ____ ____ ____ ___ ____ ____ 
|  | |__| |    |  | |__/ |__| |\ |  |     | |\ | |___ |  |    | __ |___ |\ | |___ |__/ |__|  |  |  | |__/ 
 \/  |  | |___ |__| |  \ |  | | \|  |     | | \| |    |__|    |__] |___ | \| |___ |  \ |  |  |  |__| |  \                                                                                                                                                                                                                                                                                                                                                                                                                                   
"""

welcome_message = """   
            - CLI Tool to view information within the video game Valorant in less than 5 minutes!
            - Improves your performance in Valorant by 100%!
            - Follow the CLI prompts to navigate the tool! Arrow keys and Enter are used for selection.
            - Kenny Tran (SWE1 Project)
"""

color_print([("red", banner)])
color_print([("orange", welcome_message)])

####################################################################################

while True:
    selection = inquirer.select(
        message="What would you like to learn more about in Valorant?",
        choices=["Agents", "Weapons", "Maps", "Armor"],
    ).execute()
    
    confirm = inquirer.confirm(message=f"You want to learn more about {selection}. Is this correct?").execute()
    if confirm is False:
        continue

    if selection == "Agents":
        agent = inquirer.select(
            message="You would like to learn more about Valorant agents. Which one?",
            choices=["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Deadlock", "Fade", "Gekko", "Harbor", "Jett", "Kayo", "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"],
        ).execute()
        
        for agent_data in data["data"]:
            if agent_data["displayName"] == agent:
                print(f"Agent Name: {agent_data['displayName']}")
                print(f"Description: {agent_data['description']}")
                print(f"Role: {agent_data['role']['displayName']}")
                print("-" * 25)
                for ability in agent_data["abilities"]:
                    print(f"Ability: {ability['displayName']}")
                    print(f"Description: {ability['description']}")
                    print()




