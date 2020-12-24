"""
Traning: Basic fighting game
"""


hero = {"Name": "Hero1",
            "Power": 122,
            "Weapon": "knife",
            "Health": 100}

print("Hero's Name' :{}".format(hero["Name"]))
print("Hero's Power'  :{}".format(hero["Power"]))
print("Hero's Weapon' :{}".format(hero["Weapon"]))


hero2 = {"Name": "Hero2",
             "Power": 70,
             "Weapon": "punch",
             "Health": 100}
def strike(striking:dict,shut_down:dict):
    minus = striking["Power"]
    shut_down["can"] = shut_down["Health"] - minus

strike(hero,hero2)
strike(hero2,hero)

print("Hero's Health':",hero["Health"])
print("Hero2's Health':",hero2["Health"])