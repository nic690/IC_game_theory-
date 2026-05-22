import re

mapa = {
    "C":    'clausula',
    "-":    'negacao',
    "V":    'disjuncao',
    "^":    'conjuncao',
    "->":   'implicacao',
    "<->":  'bicondicional',
    "+":    'soma',
    "*":    'produto',
    "max":  'maximo',
    "min":  'minimo',
}

nomesSAT = {
    'clausula':      'Clause       ',
    'negacao':       'Negation     ',
    'disjuncao':     'Disjunction  ',
    'conjuncao':     'Conjunction  ',
    'implicacao':    'Implication  ',
    'bicondicional': 'Biconditional',
    'soma':          'Sum          ',
    'produto':       'Product      ',
    'maximo':        'Maximum      ',
    'minimo':        'Minimum      ',
}


_TOKENS = re.compile(r'\(|\)|<->|->|max|min|\^|V|\*|\+|-|\d+')

def tokenizar(formula: str) -> list:
    return _TOKENS.findall(formula)


OP_BINARIOS = {'V', '^', '->', '<->', '+', '*', 'max', 'min'}

class Parser:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.pos = 0

    def ver(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consumir(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def parse(self):
        arvore = self._expr()
        if self.pos < len(self.tokens):
            raise ValueError(f"token inesperado: '{self.ver()}'")
        return arvore

    def _expr(self):
        esquerda = self._atomo()
        while self.ver() in OP_BINARIOS:
            op = self.consumir()
            direita = self._atomo()
            esquerda = (op, [esquerda, direita])
        return esquerda

    def _atomo(self):
        tok = self.ver()

        if tok == '(':
            self.consumir()
            expr = self._expr()
            self.consumir()
            return expr

        elif tok == '-':
            self.consumir()
            operando = self._atomo()
            return ('-', [operando])

        elif tok is not None and tok.isdigit():
            self.consumir()
            return ('C', tok)

        else:
            raise ValueError(f"nao sei o que fazer com: '{tok}'")


def _achatar(no, unidades: list) -> str:
    if no[0] == 'C':
        return no[1]

    op, filhos = no
    refs = [_achatar(filho, unidades) for filho in filhos]
    unidades.append((op, ' '.join(refs)))
    return str(len(unidades))


class Tradutor:
    def __init__(self):
        self.string = 'Sat'

    def parsear(self, formula: str) -> list:
        tokens = tokenizar(formula)
        arvore = Parser(tokens).parse()
        unidades = []
        _achatar(arvore, unidades)
        return unidades

    def traduzir(self, unidades: list) -> str:
        linhas = []
        for i, (simbolo, args) in enumerate(unidades, 1):
            op = mapa.get(simbolo, simbolo)
            linhas.append(f'Unit {i} :: {nomesSAT[op]} :: {args}')
        return '\n'.join(linhas)

    def traduzirFormula(self, formula: str) -> str:
        return self.traduzir(self.parsear(formula))


if __name__ == '__main__':
    t = Tradutor()

    testes = [
        "(1 ^ 2) V (- 1)",
        "((1 -> 2) ^ (2 -> 3)) -> (1 -> 3)",
        "(1 <-> 2)",
    ]

    for formula in testes:
        print(f"formula: {formula}")
        print(t.traduzirFormula(formula))
        print()