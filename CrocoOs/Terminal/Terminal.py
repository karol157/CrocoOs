import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import app

with open("CrocoOs\\user_info.json", "r") as file:
    json_data = json.load(file)

user = json_data.get("name")
host = json_data.get("host")

print("-------------------")
print("------ Hello ------")
print("-------------------")

print("\n")

def main():
    while True:
        data = input(f"{user}@{host}: ")

        if 'exit' in data:
            sys.exit()
        elif 'shutdown' in data:
            app.off_sys()
