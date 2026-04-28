from geradorDeJogos.gerador import jogo

class calculo_de_p(jogo):
  def __init__(self,numJogadores:int,nJogadas:int, rangeDePontuacao:int):
    super().__init__(numJogadores,nJogadas,rangeDePontuacao)
    self.jogadasDoJogador1 = []
    self.jogadasDoJogador2 = []
    self.atribuirJogadas()
    self.Mapeamento_puro()

  def atribuirJogadas(self):
    for i in range(self.nJogadas):
        self.jogadasDoJogador1.append([])
        self.jogadasDoJogador2.append([])

        for j in range(self.nJogadas):
            self.jogadasDoJogador1[i].append(self.jogo[i][j][0])
            self.jogadasDoJogador2[i].append(self.jogo[i][j][1])
            
    print("jogos para cada jogador")
    print(self.jogadasDoJogador1)
    print(self.jogadasDoJogador2)

  def Mapeamento_puro(self):
        
        n = self.nJogadas 
        combinacoes = []

       
        for i in range(n):
            
            for j in range(n):
       
                u1 = self.jogadasDoJogador1[i][j]
                u2 = self.jogadasDoJogador2[i][j]
                
               
                mapeamento = {
                    "perfil": (f"a{i+1}", f"b{j+1}"),
                    "utilidades": (u1, u2)
                }
                combinacoes.append(mapeamento)
        

        print("\n--- Mapeamento Puro hahahha deu Certo ---")
        for c in combinacoes:
            print(f"Ação {c['perfil']}: Ganhos {c['utilidades']}")
            
        return combinacoes

    
    
atribuir =calculo_de_p(2,2,100)

