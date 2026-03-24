from dataclasses import dataclass

@dataclass
class Uniforme:
    id: str
    nome: str
    tamanho: str
    quantidade: int
    valor: float

    def valor_total(self):
        return self.quantidade * self.valor
    
    def estoque_atual(self,quantidade):
        return self.quantidade > 0
    
    def adicionar_estoque(self, qtd):
        self.quantidade += qtd

    def remover_estoque (self, qtd):
        self.quantidade -= qtd

    
class Funcionario:
    id: str
    nome: str
    cpf: str
    setor: str

    def exibir_dados(self):
        return f"{self.nome} - {self.setor}"
    def mudar_setor(self, novo_setor):
        self.setor = novo_setor