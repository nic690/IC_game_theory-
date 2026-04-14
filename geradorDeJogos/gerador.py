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
    return num_inteiro

jogo1=jogo(2,3,100)



print(jogo1.jogo)






