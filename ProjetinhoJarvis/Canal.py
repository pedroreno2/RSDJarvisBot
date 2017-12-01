class Canal:
    
    def __init__(self, nomeDono, nomeCanal, linkCanal, dataCriado, qtdVideos):
        self.nomeDono   = nomeDono
        self.nomeCanal  = nomeCanal
        self.linkCanal  = linkCanal
        self.dataCriado = dataCriado
        self.qtdVideos  = qtdVideos

    
#Gets
    def getNomeDono(self):
        return self.nomeDono

    def getNomeCanal(self):
        return self.nomeCanal

    def getLinkCanal(self):
        return self.linkCanal

    def getDataCriado(self):
        return self.dataCriado

    def getQtdVideos(self):
        return self.qtdVideos

    def getAll(self):
        print('Canal: ' + self.nomeCanal)
        print('Dono : ' + self.nomeDono)
        print('Link : ' + self.linkCanal)
        print('Quantidade de Vídeos: %d'  %self.qtdVideos)
        print('Data de Criação: ' + self.dataCriado)

    def botGetAll(self):
        return self.getNomeCanal() + '  -  ' + str(self.getQtdVideos()) + ' Vídeos' + '\nCriado: ' + self.getDataCriado() + '\n\nLink: ' + self.getLinkCanal()

#Sets
    def setNomeDono(self, nd):
        self.nomeDono = nd

    def setNomeCanal(self, nc):
        self.nomeCanal = nc

    def setLinkCanal(self, lc):
        self.linkCanal = lc

    def setDataCriado(self, dc):
        self.dataCriado = dc

    def setQtdVideos(self, qv):
        self.qtdVideos = qv
