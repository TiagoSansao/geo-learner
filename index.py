import json
import random
import os
from unidecode import unidecode
from typing import List, Dict
from controllers.colors import colors

__author__ = "Tiago Sansão"
__maintainer__ = "Tiago Sansão"
__github__ = "https://github.com/TiagoSansao/geo-learner"
__version__ = "1.0.0"
__contact__ = "tiagossansao@gmail.com"

mode: int
africa, america, europa, asia, oceania = [], [], [], [], []

class PersonalData:
    def __init__(self):
        if not os.path.isfile("personal-data.json"):
            data: List[Dict[str, str]] = self.getDefaultData()
            for country in data:
                country["hits"] = 0
            self.set(data)

    def getDefaultData(self) -> List[Dict[str, str]]:
        with open("data.json", "r", encoding="utf") as default_data:
            data = json.load(default_data)
        return data

    def get(self) -> List[Dict[str, str]]:
        with open("personal-data.json", "r", encoding="utf") as personal_data:
            data: List[Dict[str, str]] = json.load(personal_data)
        return data

    def set(self, newJsonDumped) -> None:
        with open("personal-data.json", "w", encoding="utf") as personal_data:
            personal_data.write(json.dumps(newJsonDumped))


# Instance of PersonalData
personalData = PersonalData()

# Organize each continent's array accordingly
for country in personalData.get():
    print("Country: ", country)
    if country["continent"] == "Ásia":
        asia.append(country)
    elif country["continent"] == "América":
        america.append(country)
    elif country["continent"] == "Europa":
        europa.append(country)
    elif country["continent"] == "Oceania":
        oceania.append(country)
    elif country["continent"] == "África":
        africa.append(country)

# Dict to match user's input with the chosen mode
modesData: Dict[str, dict] = {
    "1": personalData.get(),
    "2": america,
    "3": europa,
    "4": africa,
    "4": oceania,
    "5": asia
}


def start():
    os.system("cls|clear")

    print(f"{colors.Cyan}Em qual continente você deseja jogar?")
    print(f"{colors.Magenta}[1]{colors.Blue} Todos")
    print(f"{colors.Magenta}[2]{colors.Blue} América")
    print(f"{colors.Magenta}[3]{colors.Blue} Europa")
    print(f"{colors.Magenta}[4]{colors.Blue} África")
    print(f"{colors.Magenta}[5]{colors.Blue} Ásia")
    print(f"{colors.Magenta}[6]{colors.Blue} Oceania")

    try:
        mode: int = int(input(f"{colors.Yellow}Resposta: {colors.White}"))
        os.system("cls|clear")
        if mode not in range(1, 7):
            return start()
    except:
        return start()

    startMode(mode)


def startMode(mode: int):
    # This block of code will set in countryData the country
    # that the player had the lowest hits 
    for modeStr in modesData:
        if str(mode) == modeStr:
            country: int = random.randrange(0, len(modesData[modeStr]) - 1)
            countryData: Dict[str, str] = modesData[modeStr][country]
            for i in range(0, 12):
                anotherCountry: int = random.randrange(
                    0, len(modesData[modeStr]) - 1)
                anotherCountryData: Dict[str,
                                         str] = modesData[modeStr][anotherCountry]
                if anotherCountryData["hits"] < countryData["hits"]:
                    countryData = anotherCountryData

    os.system("cls|clear")

    print(
        f"{colors.Cyan}Qual é a capital do país {colors.Bold}{colors.LightCyan}{countryData['name']}{colors.ResetAll}{colors.Cyan} situado na {countryData['continent']}?"
    )

    answer: str = str(input(f"{colors.Yellow}Sua resposta: {colors.White}"))
    isCorrect: bool = unidecode(str.lower(answer).strip()) == unidecode(str.lower(
        countryData["capital"]).strip())
    state: str = colors.Green + \
        "[Correto] " if isCorrect else colors.Red + "[Errado] "

    if isCorrect:
        with open("personal-data.json", "r") as f:
            data = json.load(f)
        count: int = 0
        for country in data:
            if country["name"] == countryData["name"]:
                data[count]["hits"] += 1
            count += 1
        with open("personal-data.json", "w") as f:
            f.write(json.dumps(data))

    print("\n" + state + colors.Green +
          "{capital}".format(capital=countryData["capital"]) + "\n")
    print(f"{colors.Magenta}[C]{colors.Blue}      para trocar de modo")
    print(f"{colors.Magenta}[X]{colors.Blue}      para sair")
    print(
        f"{colors.Magenta}[ENTER]{colors.Blue}  para continuar no modo"
    )

    willContinue: str = str.lower(str(input()))

    if willContinue == "c":
        start()
    elif willContinue == "x":
        exit()
    else:
        startMode(mode)


# Start the game after everything has been interpreted
start()
