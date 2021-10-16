import json
import random
import os
from controllers.colors import colors

mode: int
africa, america, europa, asia, oceania = [], [], [], [], []

with open("data.json", "r", encoding="utf") as f:
    data = json.load(f)

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

modesData: dict = {
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
        mode = int(input(f"{colors.Yellow}Resposta: {colors.White}"))
        os.system("cls|clear")
        if mode not in range(1, 7):
            return start()
    except:
        return start()
    startMode(mode)


def startMode(mode: int):
    for modeStr in modesData:
        if str(mode) == modeStr:
            country = random.randrange(0, len(modesData[modeStr]) - 1)
            countryData = modesData[modeStr][country]

    os.system("cls|clear")

    print("{d}Qual é a capital do país {b}{c}{country}{rmb}{d} situado na {continent}?".format(
        continent=countryData["continent"], country=countryData["name"], c=colors.LightCyan, d=colors.Cyan, b=colors.Bold, rmb=colors.ResetAll)
    )

    answer = str(input(f"{colors.Yellow}Sua resposta: {colors.White}"))
    isCorrect = str.lower(answer).strip() == str.lower(
        countryData["capital"]).strip()
    state = colors.Green + \
        "[Correto] " if isCorrect else colors.Red + "[Errado] "

    print("\n" + state + colors.Green +
          "{capital}".format(capital=countryData["capital"]) + "\n")
    print(f"{colors.Magenta}[C]{colors.Blue}      para trocar de modo")
    print(f"{colors.Magenta}[X]{colors.Blue}      para sair")
    print(
        f"{colors.Magenta}[ENTER]{colors.Blue}  para continuar no modo")

    willContinue = str.lower(str(input()))

    if willContinue == "c":
        start()
    elif willContinue == "x":
        exit()
    else:
        startMode(mode)


start()
