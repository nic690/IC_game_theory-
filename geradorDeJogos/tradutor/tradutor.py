
# mapa de simbolos para nomes das operacoes
mapa = {
    "C":    'clausula',        # clausula / literal
    "-":    'negacao',         # negacao (nao)
    "V":    'disjuncao',       # disjuncao (ou)
    "^":    'conjuncao',       # conjuncao (e)
    "->":   'implicacao',      # implicacao
    "<->":  'bicondicional',   # bicondicional
    "+":    'soma',            # soma de Lukasiewicz
    "*":    'produto',         # produto de Lukasiewicz
    "max":  'maximo',          # maximo
    "min":  'minimo',          # minimo
}

# nomes no padrao SAT
nomesSAT = {
    'clausula':      'Clause     ',
    'negacao':       'Negation   ',
    'disjuncao':     'Disjunction',
    'conjuncao':     'Conjunction',
    'implicacao':    'Implication',
    'bicondicional': 'Biconditional',
    'soma':          'Sum        ',
    'produto':       'Product    ',
    'maximo':        'Maximum    ',
    'minimo':        'Minimum    ',
}


class Tradutor:
    def __init__(self, string):
        self.string = 'Sat'

    def traduzir(self, unidades: list) -> str:
        # unidades e uma lista de tuplas (simbolo, argumentos)
        # ex: [('C','1 2'), ('-','1'), ('C','3'), ('V','2 3')]
        linhas = []
        for i, (simbolo, args) in enumerate(unidades, 1):
            op = mapa.get(simbolo, simbolo)
            linhas.append(f'Unit {i} :: {nomesSAT[op]} :: {args}')
        return '\n'.join(linhas)

    def fazerFuncao(self, unidades: list) -> None:
        self.string += '\n\nf:\n'
        self.string += self.traduzir(unidades) + '\n'