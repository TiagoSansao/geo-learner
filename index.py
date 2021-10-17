import json
import random
import os
from typing import List, Dict
from controllers.colors import colors

__author__ = "Tiago Sansão"
__maintainer__ = "Tiago Sansão"
__github__ = "https://github.com/TiagoSansao/geo-learner"
__version__ = "1.0.0"
__contact__ = "tiagossansao@gmail.com"

mode: int
africa, america, europa, asia, oceania = [], [], [], [], []

with open("data.json", "r", encoding="utf") as f:
    data: List[Dict[str, str]] = json.load(f)

for country in data:
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

modesData: Dict[str, dict] = {
    "1": data,
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
    for modeStr in modesData:
        if str(mode) == modeStr:
            country: int = random.randrange(0, len(modesData[modeStr]) - 1)
            countryData: Dict[str, str] = modesData[modeStr][country]

    os.system("cls|clear")

    print(
        f"{colors.Cyan}Qual é a capital do país {colors.Bold}{colors.LightCyan}{countryData['name']}{colors.ResetAll}{colors.Cyan} situado na {countryData['continent']}?"
    )

    answer: str = str(input(f"{colors.Yellow}Sua resposta: {colors.White}"))
    isCorrect: bool = str.lower(answer).strip() == str.lower(
        countryData["capital"]).strip()
    state: str = colors.Green + \
        "[Correto] " if isCorrect else colors.Red + "[Errado] "

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


start()
