# IC Game Theory

Iniciação Científica em Teoria dos Jogos.

## Estrutura do Projeto

```
IC_game_theory-/
├── geradorDeJogos/
│   ├── gerador.py                  # Classe base: gera matrizes de payoff aleatórias
│   ├── testeGerador.py             # Gera 50 jogos em lote e salva em dados.json
│   └── probabilidade/
│       └── caluculo_de_p.py        # Separa payoffs por jogador e faz mapeamento puro
└── README.md
```

## Pré-requisitos

- **Python 3.6+** instalado ([download aqui](https://www.python.org/downloads/))

Verifique se o Python está instalado:

```bash
python --version
```

## Como executar o `caluculo_de_p`

1. Abra um terminal (PowerShell, CMD ou terminal do VS Code).

2. Navegue até a **raiz do projeto**:

```bash
cd caminho/para/IC_game_theory-
```

3. Execute com o seguinte comando:

```bash
python -m geradorDeJogos.probabilidade.caluculo_de_p
```

### Saída esperada

O script irá:

1. Gerar uma matriz de jogo aleatória para 2 jogadores com 2 estratégias cada
2. Separar os payoffs de cada jogador em matrizes individuais
3. Exibir o **mapeamento puro** — todas as combinações de ações com os ganhos de cada jogador

Exemplo de saída:

```
Montando matriz do jogo
[(87, 66), (68, 75)]
[(20, 40), (2, 30)]

jogos para cada jogador
[[87, 68], [20, 2]]
[[66, 75], [40, 30]]

--- Mapeamento Puro ---
Ação ('a1', 'b1'): Ganhos (87, 66)
Ação ('a1', 'b2'): Ganhos (68, 75)
Ação ('a2', 'b1'): Ganhos (20, 40)
Ação ('a2', 'b2'): Ganhos (2, 30)
```

> **Nota:** Os valores dos payoffs são gerados aleatoriamente, então os números serão diferentes a cada execução.

## Como executar o gerador de jogos em lote

Para gerar 50 jogos e salvar em `dados.json`:

```bash
cd geradorDeJogos
python testeGerador.py
```

O arquivo `dados.json` será criado na pasta `geradorDeJogos/`.
