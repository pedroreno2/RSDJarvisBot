from Canal import Canal



class Instrutor:

    def __init__(self, n, dn, c, progs, sobre):
        self.nome      = n
        self.dataNasc  = dn
        self.canal     = c
        self.programas = progs
        self.sobre     = sobre




#Gets
    def getNome(self):
        return self.nome

    def getDataNasc(self):
        return self.dataNasc

    def getCanal(self):
        return self.canal.getNomeCanal()

    def getProgramas(self):
        progs = ''

        for x in range(len(self.programas) ):
            progs += self.programas[x] + ', '

        progs = progs[:-2]
        return progs

    def getSobre(self):
        return self.sobre

    def getAll(self):

        print('Nome: ' +             + self.nome)
        print('Data de Nascimento: ' + self.dataNasc)
        print('Canal: ',             + self.getCanal() )
        print('Programas: ',         + self.programas)

    def botGetAll(self):

        return 'Nome: '               + self.getNome() +\
               '\nBirthday: '         + self.getDataNasc() +\
               '\nYoutube Chanel: '  + self.getCanal() +\
               '\nProgramas: '        + self.getProgramas()





#Sets
    def setNome(self, n):
        self.nome = n

    def setDataNasc(self, dn):
        self.dataNasc = dn

    def setCanal(self, c):
        self.canal = c

    #Criar um setProgramas
