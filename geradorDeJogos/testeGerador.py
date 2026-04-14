from gerador import jogo
from pathlib import Path

import json


def salvar_jogos(lista_jogos):
    with open("dados.json", "w") as f:
        json.dump(lista_jogos, f, indent=4)

todos_os_jogos = []

contador = 0
while contador < 50:
    jogo1 = jogo(2, 5, 100)
    todos_os_jogos.append(jogo1.jogo)
    contador += 1

salvar_jogos(todos_os_jogos)
print(f" {len(todos_os_jogos)} jogos salvos em dados.json")
