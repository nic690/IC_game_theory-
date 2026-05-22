import os


class TxtM:
    """Classe para manipulação de arquivos .txt"""

    def __init__(self, caminho: str):
        """
        Inicializa o manipulador de arquivos txt.

        Args:
            caminho: caminho do arquivo .txt (ex: 'dados/resultado.txt')
        """
        self.caminho = caminho
        self.criar()

    def criar(self):
        """Cria o arquivo se ele ainda não existir. Cria as pastas intermediárias também."""
        pasta = os.path.dirname(self.caminho)
        if pasta and not os.path.exists(pasta):
            os.makedirs(pasta)

        if not os.path.exists(self.caminho):
            with open(self.caminho, "w", encoding="utf-8") as f:
                pass  # cria o arquivo vazio
            print(f"Arquivo criado: {self.caminho}")
        else:
            print(f"Arquivo já existe: {self.caminho}")

    def escrever(self, texto: str):
        """
        Adiciona uma linha ao final do arquivo.

        Args:
            texto: conteúdo a ser escrito
        """
        with open(self.caminho, "a", encoding="utf-8") as f:
            f.write(texto + "\n")
        print(f"Escrito: {texto}")

    def ultima_linha(self) -> str:
        """
        Retorna a última linha do arquivo.

        Returns:
            A última linha como string, ou uma mensagem se o arquivo estiver vazio.
        """
        with open(self.caminho, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        if not linhas:
            print("O arquivo está vazio.")
            return ""

        ultima = linhas[-1].strip()
        print(f"Última linha: {ultima}")
        return ultima


if __name__ == "__main__":
    # Exemplo de uso
    arquivo = TxtM("exemplo.txt")

    arquivo.escrever("Primeira linha de teste")
    arquivo.escrever("Segunda linha de teste")
    arquivo.escrever("Terceira linha de teste")

    resultado = arquivo.ultima_linha()
