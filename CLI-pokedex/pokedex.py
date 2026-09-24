import json

file = open("pokedex.json")
pokemon = json.load(file)
file.close()

name = input("Enter the name of the Pokemon: ")
print ("Searching for " + name + "...")
for p in pokemon:
    if p["name"] == name:
        print("Found it!")
        print(p["name"] + " is a " + p["type"] + " type Pokemon. Weaknesses: " + str(p["weaknesses"]) + ".")
