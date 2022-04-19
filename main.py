
import copy
import time
import pygame


# . - - . - - .
# | . - . - . |
# | | . . . | |
# . . . _ . . .
# | | . . . | |
# | . - . - . |
# . - - . - - .

adancimeMax = 1

def createTable():
    l = []
    l.append(['.', '-', '-', '.', '-', '-', '.'])
    l.append(['|', '.', '-', '.', '-', '.', '|'])
    l.append(['|', '|', '.', '.', '.', '|', '|'])
    l.append(['.', '.', '.', '-', '.', '.', '.'])
    l.append(['|', '|', '.', '.', '.', '|', '|'])
    l.append(['|', '.', '-', '.', '-', '.', '|'])
    l.append(['.', '-', '-', '.', '-', '-', '.'])
    return l

class Joc:

    lungime = 7
    JMIN = None  # tu
    JMAX = None  # ai
    tbla = createTable()
    etapa = 1               # in ce stadiu al jocului ne aflam 1 = punem piese; 2 mutam piesele puse

    nrPieseA = 9
    nrPieseN = 9

    def __init__(self, tabla=None):  # Joc()
        self.matr = tabla or Joc.tbla

    @classmethod
    def jucator_opus(cls, jucator):
        # val_true if conditie else val_false
        return cls.JMAX if jucator == cls.JMIN else cls.JMIN

    def final(self):
        if self.nrPieseN == 2:
            print("A castiga")
            return 'A'
        if self.nrPieseA == 2:
            print("N castiga")
            return 'N'
        return False

    def mutari(self, jucator):  # jucator = simbolul jucatorului care muta
        if self.etapa == 1:
            l_mutari = []
            for i in range(self.lungime):
                for j in range(self.lungime):
                    if self.matr[i][j] == '.':
                        copie_matr = copy.deepcopy(self.matr)
                        copie_matr[i][j] = jucator
                        l_mutari.append(Joc(copie_matr))
            return l_mutari
        if self.etapa == 2:
            l_mutari = []
            #layer1 colturi
            if self.matr[0][0] == jucator:
                if self.matr[0][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[0][3] = jucator
                    copie_matr[0][0] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[3][0] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][0] = jucator
                    copie_matr[0][0] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[0][6] == jucator:
                if self.matr[0][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[0][3] = jucator
                    copie_matr[0][6] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[3][6] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][6] = jucator
                    copie_matr[0][6] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[6][6] == jucator:
                if self.matr[6][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[6][3] = jucator
                    copie_matr[6][6] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[3][6] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][6] = jucator
                    copie_matr[6][6] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[6][0] == jucator:
                if self.matr[0][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[0][3] = jucator
                    copie_matr[6][0] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[6][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[6][3] = jucator
                    copie_matr[6][0] = '.'
                    l_mutari.append(Joc(copie_matr))

            # layer1 mijloc
            if self.matr[0][3] == jucator:
                if self.matr[0][0] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[0][0] = jucator
                    copie_matr[0][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[0][6] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[0][6] = jucator
                    copie_matr[0][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[1][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[1][3] = jucator
                    copie_matr[0][3] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[3][0] == jucator:
                if self.matr[0][0] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[0][0] = jucator
                    copie_matr[3][0] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[6][0] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[6][0] = jucator
                    copie_matr[3][0] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[3][1] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][1] = jucator
                    copie_matr[3][0] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[6][3] == jucator:
                if self.matr[6][6] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[6][6] = jucator
                    copie_matr[6][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[6][0] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[6][0] = jucator
                    copie_matr[6][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[5][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[5][3] = jucator
                    copie_matr[6][3] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[3][6] == jucator:
                if self.matr[6][6] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[6][6] = jucator
                    copie_matr[3][6] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[0][6] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[0][6] = jucator
                    copie_matr[3][6] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[3][5] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][5] = jucator
                    copie_matr[3][6] = '.'
                    l_mutari.append(Joc(copie_matr))

            # layer2 colturi
            if self.matr[1][1] == jucator:
                if self.matr[1][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[1][3] = jucator
                    copie_matr[1][1] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[3][1] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][1] = jucator
                    copie_matr[1][1] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[1][5] == jucator:
                if self.matr[1][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[1][3] = jucator
                    copie_matr[1][5] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[3][5] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][5] = jucator
                    copie_matr[1][5] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[5][5] == jucator:
                if self.matr[5][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[5][3] = jucator
                    copie_matr[5][5] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[3][5] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][5] = jucator
                    copie_matr[5][5] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[5][1] == jucator:
                if self.matr[5][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[5][3] = jucator
                    copie_matr[5][1] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[3][1] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][1] = jucator
                    copie_matr[5][1] = '.'
                    l_mutari.append(Joc(copie_matr))

            # layer2 mijloc
            if self.matr[1][3] == jucator:
                if self.matr[0][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[0][3] = jucator
                    copie_matr[1][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[2][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[2][3] = jucator
                    copie_matr[1][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[1][1] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[1][1] = jucator
                    copie_matr[1][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[1][5] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[1][5] = jucator
                    copie_matr[1][3] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[3][1] == jucator:
                if self.matr[3][0] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][0] = jucator
                    copie_matr[3][1] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[3][2] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][2] = jucator
                    copie_matr[3][1] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[1][1] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[1][1] = jucator
                    copie_matr[3][1] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[5][1] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[5][1] = jucator
                    copie_matr[3][1] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[5][3] == jucator:
                if self.matr[4][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[4][3] = jucator
                    copie_matr[5][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[6][1] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[6][1] = jucator
                    copie_matr[5][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[5][5] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[5][5] = jucator
                    copie_matr[5][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[5][1] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[5][1] = jucator
                    copie_matr[5][3] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[3][5] == jucator:
                if self.matr[3][4] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][4] = jucator
                    copie_matr[3][5] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[1][6] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[1][6] = jucator
                    copie_matr[3][5] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[5][5] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[5][5] = jucator
                    copie_matr[3][5] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[1][5] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[1][5] = jucator
                    copie_matr[3][5] = '.'
                    l_mutari.append(Joc(copie_matr))

            #layer3 margini
            if self.matr[2][2] == jucator:
                if self.matr[2][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[2][3] = jucator
                    copie_matr[2][2] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[3][2] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][2] = jucator
                    copie_matr[2][2] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[2][4] == jucator:
                if self.matr[2][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[2][3] = jucator
                    copie_matr[2][4] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[3][4] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][4] = jucator
                    copie_matr[2][4] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[4][4] == jucator:
                if self.matr[3][4] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][4] = jucator
                    copie_matr[4][4] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[4][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[4][3] = jucator
                    copie_matr[4][4] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[4][2] == jucator:
                if self.matr[3][2] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][2] = jucator
                    copie_matr[4][2] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[4][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[4][3] = jucator
                    copie_matr[4][2] = '.'
                    l_mutari.append(Joc(copie_matr))

            #layer3 mijloc
            if self.matr[2][3] == jucator:
                if self.matr[1][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[1][3] = jucator
                    copie_matr[2][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[2][4] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[2][4] = jucator
                    copie_matr[2][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[2][2] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[2][2] = jucator
                    copie_matr[2][3] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[3][4] == jucator:
                if self.matr[3][5] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][5] = jucator
                    copie_matr[3][4] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[2][4] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[2][4] = jucator
                    copie_matr[3][4] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[4][4] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[4][4] = jucator
                    copie_matr[3][4] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[4][3] == jucator:
                if self.matr[5][3] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[5][3] = jucator
                    copie_matr[4][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[4][2] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[4][2] = jucator
                    copie_matr[4][3] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[4][4] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[4][4] = jucator
                    copie_matr[4][3] = '.'
                    l_mutari.append(Joc(copie_matr))

            if self.matr[3][2] == jucator:
                if self.matr[3][1] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[3][1] = jucator
                    copie_matr[3][2] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[4][2] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[4][2] = jucator
                    copie_matr[3][2] = '.'
                    l_mutari.append(Joc(copie_matr))
                if self.matr[2][2] == '.':
                    copie_matr = copy.deepcopy(self.matr)
                    copie_matr[2][2] = jucator
                    copie_matr[3][2] = '.'
                    l_mutari.append(Joc(copie_matr))

            return l_mutari
        return []

    def linieDeschisa(self,l,jucator):
        jo = self.jucator_opus(jucator)
        if not jo in self.matr[l]:
            return 1
        return 0
    def cololanaDeschisa(self,c,jucator):
        jo = self.jucator_opus(jucator)
        for i in range(self.lungime):
            if self.matr[i][c] == jo:
                return 0
        return 1

    def linColDeschise(self,jucator):
        nr = 0
        for i in range(self.lungime):
            nr += self.linieDeschisa(i,jucator)
            nr += self.cololanaDeschisa(i,jucator)
        return nr


    def linieIdentica(self,l,jucator):
        if self.matr[l].count(jucator) == 3:
            return True
        return False

    def coloanaIdentica(self,c,jucator):
        nr = 0
        for i in range(self.lungime):
            if self.matr[i][c] == jucator:
                nr +=1
        return nr == 3

    def estimeazaScor(self,adancime):   #?
        tFinal = self.final()
        if tFinal == self.__class__.JMAX:  # self.__class__ referinta catre clasa instantei
            return (99 + adancime)
        elif tFinal == self.__class__.JMIN:
            return (-99 - adancime)
        elif tFinal == 'remiza':
            return 0
        else:
            return (self.linColDeschise(self.__class__.JMAX) - self.linColDeschise(self.__class__.JMIN))

    # def sirAfisare(self):
    #     sir = ''
    #     for li in self.matr:
    #         for elem in li:
    #             sir += str(elem) + ' '
    #         sir += '\n'
    #     return sir
    def sirAfisare(self):
        sir = "  | "
        sir += " ".join([str(i) for i in range(self.lungime)]) + "\n"
        sir += "-" * ((self.lungime + 1) * 2+1) + "\n"
        # for i in range(self.lungime):  # itereaza prin linii
        #     sir += str(i) + " |" + " ".join(
        #         [str(x) for x in self.matr[self.lungime * i: self.lungime * (i + 1)]]) + "\n"
        i = 0
        for li in self.matr:
            sir += str(i) + ' | '
            i+= 1
            for elem in li:
                    sir += str(elem) + ' '
            sir += '\n'
        # [0,1,2,3,4,5,6,7,8]
        return sir

    def __str__(self):
        return  self.sirAfisare()

    def __repr__(self):
        return self.sirAfisare()
# . - - . - - .
# | . - . - . |
# | | . . . | |
# . . . _ . . .
# | | . . . | |
# | . - . - . |
# . - - . - - .

class Stare:

    def __init__(self, tablaJoc, jucatorCurent, adancime, parinte=None, estimare=None):
        self.tablaJoc = tablaJoc            # ob Joc
        self.jucatorCurent = jucatorCurent
        self.adancime = adancime

        self.estimare = estimare
        self.mutariPosibile = []
        self.stareAleasa = None

    def mutari(self):
        listMutari = self.tablaJoc.mutari(self.jucatorCurent)
        jucatorOpus = self.tablaJoc.jucator_opus(self.jucatorCurent)

        listStari = [Stare(mutare,jucatorOpus, self.adancime - 1,parinte= self) for mutare in listMutari]

        return  listStari

    def __str__(self):
        sir = str(self.tablaJoc) + "(Juc curent:" + self.jucatorCurent + ")\n"
        return sir


def min_max(stare):
    # daca sunt la o frunza in arborele minimax sau la o stare finala
    if stare.adancime == 0 or stare.tablaJoc.final():
        stare.estimare = stare.tablaJoc.estimeazaScor(stare.adancime)
        return stare

    # calculez toate mutarile posibile din starea curenta
    stare.mutariPosibile = stare.mutari()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutariCuEstimare = [min_max(x) for x in stare.mutariPosibile]  # expandez(constr subarb) fiecare nod x din mutari posibile

    if stare.jucatorCurent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu estimarea maxima
        stare.stareAleasa = max(mutariCuEstimare, key=lambda x: x.estimare)  # def f(x): return x.estimare -----> key=f
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu estimarea minima
        stare.stareAleasa = min(mutariCuEstimare, key=lambda x: x.estimare)

    stare.estimare = stare.stareAleasa.estimare
    return stare



def afis_daca_final(stare_curenta):
    final = stare_curenta.tablaJoc.final()  # metoda final() returneaza "remiza" sau castigatorul ("x" sau "0") sau False daca nu e stare finala
    if (final):
        if (final == "remiza"):
            print("Remiza!")
        else:
            print("A castigat " + final)

        return True

    return False



def main():
    raspunsV = False

    while not raspunsV:
        tip_algoritm = input("Algoritmul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1', '2']:
            raspunsV = True
        else:
            print("Nu ati ales o varianta corecta.")

    raspunsV = False
    while not raspunsV:
        Joc.JMIN = input("Doriti sa jucati cu a sau cu n? ").lower()
        if (Joc.JMIN in ['a', 'n']):
            raspunsV = True
        else:
            print("Raspunsul trebuie sa fie a sau n.")

    Joc.JMAX = 'n' if Joc.JMIN == 'a' else 'a'

    # initializare tabla
    tablaC = Joc()
    print("Tabla initiala")
    print(str(tablaC))

    # creare stare initiala
    stareC = Stare(tablaC,'a',adancimeMax)

    while True:
        if stareC.tablaJoc.etapa == 1:
            if(stareC.jucatorCurent == Joc.JMIN): #daca e randul tau
                print("Acum muta utilizatorul cu simbolul", stareC.jucatorCurent)
                raspunsV = False
                while not raspunsV:
                    try:
                        linie = int(input("linie="))
                        coloana = int(input("coloana="))
                        if linie in range(Joc.lungime) and coloana in range(Joc.lungime):
                            if stareC.tablaJoc.matr[linie][coloana] == '.':
                                raspunsV = True
                            else:
                                print("Aici nu se poate pune piesa")
                        else:
                            print("nu sunt coord bune")

                    except ValueError:
                        print("Linia si coloana trebuie sa fie numere intregi")
                # dupa iesirea din while sigur am valide atat linia cat si coloana
                # deci pot plasa simbolul pe "tabla de joc"
                stareC.tablaJoc.matr[linie][coloana] = Joc.JMIN

                # afisarea starii jocului in urma mutarii utilizatorului
                print("\nTabla dupa mutarea jucatorului")
                print(str(stareC))

                # testez daca jocul a ajuns intr-o stare finala
                # si afisez un mesaj corespunzator in caz ca da
                if (afis_daca_final(stareC)):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                stareC.jucatorCurent = Joc.jucator_opus(stareC.jucatorCurent)

            else:      # randu ai
                print("Acum muta calculatorul cu simbolul", stareC.jucatorCurent)
                # preiau timpul in milisecunde de dinainte de mutare
                t_inainte = int(round(time.time() * 1000))

                # stare actualizata e starea mea curenta in care am setat stare_aleasa (mutarea urmatoare)
                if tip_algoritm == '1':
                    stare_actualizata = min_max(stareC)
                # else:  # tip_algoritm==2
                #     stare_actualizata = alpha_beta(-500, 500, stare_curenta)
                stareC.tablaJoc = stare_actualizata.stareAleasa.tablaJoc  # aici se face de fapt mutarea !!!
                print("Tabla dupa mutarea calculatorului")
                print(str(stareC))

                # preiau timpul in milisecunde de dupa mutare
                t_dupa = int(round(time.time() * 1000))
                print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")
                # TO DO 8b
                if (afis_daca_final(stareC)):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                stareC.jucatorCurent = Joc.jucator_opus(stareC.jucatorCurent)


if __name__ == "__main__":
    main()




