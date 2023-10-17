class Pessoa():
    nome = "";
    idade = 0;
    altura = 0;
    peso = 0;
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome;
        self.idade = idade;
        self.altura = altura;
        self.peso = peso;

    def resumoGen(self):
        print(f"Eu sou {self.nome} \neu tenho {self.altura} de altura, \n{self.peso} de peso \ne {self.idade} de idade");
        print("=====================================================")

class Pai(Pessoa):
    def __init__(self, nome, idade, altura, peso, cabelo):
        super().__init__(nome, idade, altura, peso);
        self.cabelo = cabelo;

    def gerarFilho(self):
        filho = Filho("José das Couve", 0, 4.5, 0.65 , mae.olhos, pai.cabelo);
        self.filhoNome = filho.nome;
        filho.resumoTotalFilho();
    
    def resumoTotalPai(self):
        print(f"Eu sou o Pai {self.nome} \neu tenho {self.altura} de altura, \n{self.peso} de peso \ne {self.idade} de idade, e tenho um filho chamado {self.filhoNome}");
        print("=====================================================");


class Mae(Pessoa):
    def __init__(self, nome, idade, altura, peso, olhos):
        super().__init__(nome, idade, altura, peso);
        self.olhos = olhos;
    
    def gerarFilho(self):
        filho = Filho("Ana", 0, 4, 0.55, mae.olhos, pai.cabelo);
        self.filhoNome = filho.nome;
        filho.resumoTotalFilho();

    def resumoTotalMae(self):
        print(f"Eu sou a Mae {self.nome} \neu tenho {self.altura} de altura, \n{self.peso} de peso \ne {self.idade} de idade, e tenho um filho chamado {self.filhoNome}");
        print("=====================================================");


class Filho(Pessoa):
    def __init__(self, nome, idade, altura, peso, olhos, cabelo):
        super().__init__(nome, idade, altura, peso);
        self.olhos = olhos;
        self.cabelo = cabelo;
    def resumoTotalFilho(self):
        print(f"Eu sou o Filho {self.nome} \neu tenho {self.altura} de altura, \n{self.peso} de peso \ne {self.idade} de idade, \ne meu cabelo é {pai.cabelo} e meus olhos são {mae.olhos}");
        print("=====================================================");

if __name__ == "__main__":
    pai = Pai("Paulo Joares", 45, 80, 180, "Loiro")
    mae = Mae("Maria Lurdes", 40, 51, 165, "Azuis")
    pai.gerarFilho();
    mae.gerarFilho();

    pai.resumoGen();
    mae.resumoGen();
    pai.resumoTotalPai();
    mae.resumoTotalMae();
