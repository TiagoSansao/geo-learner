import json
import random
import os

mode: int
data = json.load(open("data.json", "r"))


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def start():
    os.system("cls|clear")
    print("Qual continente você deseja jogar?")
    print("[1] Todos")
    print("[2] América")
    print("[3] Europa")
    print("[4] África")
    print("[5] Ásia")
    print("[6] Oceania")
    mode = int(input("Insira o número do modo que você deseja: "))
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
    print("Qual é a capital do país {country} situado no(a) {continent}?".format(
        continent=countryData["continent"], country=countryData["name"])
    )
    answer = str(input())
    isCorrect = answer == data[country]["capital"]
    state = "Resposta correta! " if isCorrect else "Resposta incorreta! "
    print(state + "A capital de {country} é {capital}.".format(
        country=countryData["name"], capital=countryData["capital"]))
    print("[C] para trocar de modo.")
    print("[X] para sair.")
    print("[Qualquer tecla] para continuar no modo.")
    willContinue = str(input())
    if willContinue == "C":
        start()
    elif willContinue == "X":
        exit()
    else:
        start()


start()
