import json
import random
import os

mode: int
data = json.load(open("data.json", "r"))
africa, america, europa, asia, oceania = [], [], [], [], []
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


class modesData:
    todos = data
    america = america
    europa = europa
    africa = africa
    asia = asia
    oceania = oceania


class colors:
    Default = "\033[39m"
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"
    ResetAll = "\033[0m"
    Bold = "\033[1m"


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
    if (mode == 1):
        country = random.randrange(0, len(modesData.todos) - 1)
        countryData = modesData.todos[country]
    elif (mode == 2):
        country = random.randrange(0, len(modesData.america) - 1)
        countryData = modesData.america[country]
    elif (mode == 3):
        country = random.randrange(0, len(modesData.europa) - 1)
        countryData = modesData.europa[country]
    elif (mode == 4):
        country = random.randrange(0, len(modesData.africa) - 1)
        countryData = modesData.africa[country]
    elif (mode == 5):
        country = random.randrange(0, len(modesData.asia) - 1)
        countryData = modesData.asia[country]
    elif (mode == 6):
        country = random.randrange(0, len(modesData.oceania) - 1)
        countryData = modesData.oceania[country]

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
