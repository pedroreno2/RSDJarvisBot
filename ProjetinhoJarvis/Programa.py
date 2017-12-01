class Programa:

    def __init__(self, nomeDono, nomeProg, dataLancamento, preco):
        self.nomeDono       = nomeDono
        self.nomeProg       = nomeProg
        self.dataLancamento = dataLancamento
        self.preco          = preco

#Gets
    def getNomeDono(self):
        return self.nomeDono

    def getNomeProg(self):
        return self.nomeProg

    def getDataLancamento(self):
        return self.dataLancamento

    def getPreco(self):
        return self.preco

    def getAll(self):
        print('Nome do Dono: ' + self.nomeDono)
        print('Nome do Programa: ' + self.nomeProg)
        print('Data de lançamento: ' + self.dataLancamento)
        print('Preço: ' + self.preco)

    def botGetAll(self):

        return 'Nome do Dono: '         + self.getNomeDono() +\
               '\nNome do Programa: '   + self.getNomeProg() +\
               '\nData de Lançamento: ' + self.getDataLancamento() +\
               '\nPreço: '              + self.getPreco()
        

#Sets
    def setNomeDono(self, nd):
        self.nomeDono = nd

    def setNomeProg(self, np):
        self.nomeProg = np

    def setDataLancamento(self, dl):
        self.dataLancamento = dl

    def setPreco(self, p):
        self.preco = p
        
