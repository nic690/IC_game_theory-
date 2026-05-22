import random
print('Gerador de jogos')

class jogo:
  def __init__(self, numJogadores:int,nJogadas:int, rangeDePontuacao:int):

      self.numJogadores=numJogadores # Número de jogadores
      self.nJogadas=nJogadas #Numero de jogadas
      self.rangeDePontuacao=rangeDePontuacao
      self.jogo=[]
      self.montarJogo()

  def montarJogo(self):
     print("Montando matriz do jogo")

     for i in range(self.nJogadas):
        self.jogo.append([])
        for j in range(self.nJogadas):
           self.jogo[i].append(self.valorDaposicao())
        print(self.jogo[i])


  def valorDaposicao(self):
    num_inteiro = random.randint(0,self.rangeDePontuacao)
    num_inteiro2 = random.randint(0,self.rangeDePontuacao)
    return (num_inteiro,num_inteiro2)

jogo1=jogo(2,3,100)



print(jogo1.jogo)

# exemplo de uso do tradutor
from tradutor.tradutor import Tradutor

t = Tradutor('')
t.fazerFuncao([
    ('C',  '1 2'),   # clausula com variaveis 1 e 2
    ('-',  '1'),     # negacao da unidade 1
    ('C',  '3'),     # clausula com variavel 3
    ('V',  '2 3'),   # disjuncao das unidades 2 e 3
])
print(t.string)


