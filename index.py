import json
import random
import os

mode: int
data = json.load(open("data.json", "r"))


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
    print(f"{colors.Cyan}Qual continente você deseja jogar?")
    print(f"{colors.Magenta}[1]{colors.Blue} Todos")
    print(f"{colors.Magenta}[2]{colors.Blue} América")
    print(f"{colors.Magenta}[3]{colors.Blue} Europa")
    print(f"{colors.Magenta}[4]{colors.Blue} África")
    print(f"{colors.Magenta}[5]{colors.Blue} Ásia")
    print(f"{colors.Magenta}[6]{colors.Blue} Oceania")
    mode = int(input(f"{colors.Yellow}Resposta: {colors.White}"))
    os.system("cls|clear")
    if mode <= 0 and mode > 6:
        print(
            "Valor: {value} não é válido, insira: 1, 2 ou 3!".format(
                value=mode)
        )
        return start()
    startMode(mode)


def startMode(mode: int):
    country = random.randrange(0, len(data) - 1)
    countryData = data[country]

    os.system("cls|clear")
    print("{d}Qual é a capital do país {b}{c}{country}{rmb}{d} situado na {continent}?".format(
        continent=countryData["continent"], country=countryData["name"], c=colors.LightCyan, d=colors.Cyan, b=colors.Bold, rmb=colors.ResetAll)
    )

    answer = str(input(f"{colors.Yellow}Sua resposta: {colors.White}"))
    isCorrect = str.lower(answer) == str.lower(data[country]["capital"])
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
