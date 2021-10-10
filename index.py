import json
import random

mode: int
data = json.load(open("data.json", "r"))


def start():
    print("Qual modo de jogo você deseja?")
    print("[1] Países")
    print("[2] Capitais de países")
    print("[3] Continentes")
    mode = int(input("Insira o número do modo que você deseja: "))
    if mode != 1 and mode != 2 and mode != 3:
        print(
            "Valor: {value} não é válido, insira: 1, 2 ou 3!".format(
                value=mode)
        )
        return start()
    startMode(mode)


def startMode(mode: int):
    country = random.randrange(0, len(data) - 1)
    print("Qual país da {continent} possui {capital} como capital?"
          .format(continent=data[country]["continent"], capital=data[country]["capital"]))
    print(":TW")


start()
