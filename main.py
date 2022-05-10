#1 linia 644 in jos  /  cine muta 1083 1300  /  daca final linia 621

#2 linia 633 pt dificultate

#3 666 - 689 initializari

#4 674 - 683 doar init pt interfata functii fol 422 478

#5 298 - functia de generare a mutarilor

#6 700 859 mutare utilizator pt etapele jocului

#7 88 stabilire stari finale

#8 403 414

#9 -

#10 703 862 1342



import copy
import time
import pygame
import sys
import math


# . - - . - - .
# | . - . - . |
# | | . . . | |
# . . . _ . . .
# | | . . . | |
# | . - . - . |
# . - - . - - .

adancimeMax = 3

culoareEcran = (255, 255, 255)
culoareLinii = (0, 0, 0)

def distEuclid(p0,p1):
    (x0,y0)=p0
    (x1,y1)=p1
    return math.sqrt((x0-x1)**2+(y0-y1)**2)


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

    nrPieseMin = 9
    nrPieseMax = 9
    piesePuseMin = 0
    piesePuseMax = 0

    scalare = 100
    translatie = 20
    razaPct = 10
    razaPiesa = 20
    noduri = []
    muchii =[]

    def __init__(self, tabla=None):  # Joc()
        self.matr = tabla or Joc.tbla

    @classmethod
    def jucator_opus(cls, jucator):
        # val_true if conditie else val_false
        return cls.JMAX if jucator == cls.JMIN else cls.JMIN

    def final(self):
        if self.nrPieseMin == 2:
            print("AI castiga ")
            return self.JMAX
        if self.nrPieseMax == 2:
            print("Tu castigi")
            return self.JMIN
        if self.estiblocat(self.JMIN) and self.etapa == 2:
            print("AI castiga ")
            return self.JMAX
        if self.estiblocat(self.JMAX) and self.etapa == 2:
            print("Tu castigi")
            return self.JMIN
        return False


    #aceasta functie verifica daca elementul de coord date face parte dintr o linie sau coloana full (aceasata verif se face doar pe piese abia mutate)
    def contineLinCol(self, linie,coloana,matrice):
        # verif de linie
        l = linie
        c = coloana
        contine = 0
        while l >= 0:
            l -= 1
            if l < 0:
                break

            if l == 3 and c == 3:
                break
            if matrice[l][c] == '|':
                continue
            if matrice[l][c] == matrice[linie][coloana]:
                contine += 1
                # break
            else:
                break

        l = linie
        c = coloana
        while l <= 6:
            l += 1
            if l > 6:
                break

            if l == 3 and c == 3:
                break
            if matrice[l][c] == '|':
                continue
            if matrice[l][c] == matrice[linie][coloana]:
                contine += 1
                # break
            else:
                break

        if contine == 2:
            return True

        contine = 0
        l = linie
        c = coloana
        while c >= 0:
            c -= 1
            if c < 0:
                break

            if l == 3 and c == 3:
                break
            if matrice[l][c] == '-':
                continue
            if matrice[l][c] == matrice[linie][coloana]:
                contine += 1
                # break
            else:
                break

        l = linie
        c = coloana
        while c <= 6:
            c += 1
            if c > 6:
                break

            if l == 3 and c == 3:
                break
            if matrice[l][c] == '-':
                continue
            if matrice[l][c] == matrice[linie][coloana]:
                contine += 1
                # break
            else:
                break

        if contine == 2:
            return True

        return False


    # aceasta functie = pentru fiecare piesa pusa pe tabla sa vada daca are mutari posibile
    def undePotiMuta(self,linie,coloana):
        lis = []
        l = linie
        c = coloana
        while c >= 0:
            c -= 1
            if c < 0:
                break

            if l == 3 and c == 3:
                break
            if self.matr[l][c] == '-':
                continue
            if self.matr[l][c] == '.':
                lis.append((l, c))
                break
            else:
                break

        l = linie
        c = coloana
        while c <= 6:
            c += 1
            if c > 6 :
                break


            if l == 3 and c == 3:
                break
            if self.matr[l][c] == '-':
                continue
            if self.matr[l][c] == '.':
                lis.append((l, c))
                break
            else:
                break

        l = linie
        c = coloana
        while l >= 0:
            l -= 1
            if l < 0:
                break

            if l == 3 and c == 3:
                break
            if self.matr[l][c] == '|':
                continue
            if self.matr[l][c] == '.':
                lis.append((l, c))
                break
            else:
                break

        l = linie
        c = coloana
        while l <= 6:
            l += 1
            if l > 6:
                break

            if l == 3 and c == 3:
                break
            if self.matr[l][c] == '|':
                continue
            if self.matr[l][c] == '.':
                lis.append((l, c))
                break
            else:
                break

        return lis


    # cand nu mai ai mutari posibile ca sa termini jocul !! folosit la final
    def estiblocat(self, jucator):  # jucator = simbolul jucatorului caruia i se ia o piesa
        list, fals = self.locatiePiese(jucator)
        for piesa in list:
            if len(self.undePotiMuta(piesa[0], piesa[1])) != 0:
                return False
        return True


    #pentru o matrice data functia genereaza toate posibilitatile de a sterge o piesa de tipul jucator
    def stergeElement(self,matrice,jucator):  # jucator = simbolul jucatorului caruia i se ia o piesa
        l_matrice = []
        for i in range(self.lungime):
            for j in range(self.lungime):
                if matrice[i][j] == jucator and self.contineLinCol(i,j,self.matr) == False:
                    copieMatrice = copy.deepcopy(matrice)
                    copieMatrice[i][j] = '.'
                    l_matrice.append(copieMatrice)
                elif matrice[i][j] == jucator and self.contineLinCol(i,j,self.matr) == True:
                    if (jucator == self.JMIN and self.nrPieseMin == 3) or (jucator == self.JMAX and self.nrPieseMax == 3):
                        copieMatrice = copy.deepcopy(matrice)
                        copieMatrice[i][j] = '.'
                        l_matrice.append(copieMatrice)


        return l_matrice

    # returneaza pozitiile unde sunt locuri libere '.'
    def locLiber(self):
        l = []
        for i in range(self.lungime):
            for j in range(self.lungime):
                if self.matr[i][j] == '.':
                    l.append([i,j])
        return l


    def mutari(self, jucator):  # jucator = simbolul jucatorului care muta
        if self.etapa == 1:
            l_mutari = []
            for i in range(self.lungime):
                for j in range(self.lungime):
                    if self.matr[i][j] == '.':
                        copie_matr = copy.deepcopy(self.matr)
                        copie_matr[i][j] = jucator
                        if self.contineLinCol(i,j,copie_matr) == False:
                            l_mutari.append(Joc(copie_matr))
                        else:
                            ceva = self.stergeElement(copie_matr, self.jucator_opus(jucator))
                            for matrice in ceva:
                                l_mutari.append(Joc(matrice))

            return l_mutari

        if self.etapa == 2 and self.nrPiese(jucator) > 3:
            l_mutari = []
            for i in range(self.lungime):
                for j in range(self.lungime):
                    if self.matr[i][j] == jucator:
                        listaMutari = self.undePotiMuta(i,j)
                        if len(listaMutari) > 0:
                            for elem in listaMutari:
                                copie_matr = copy.deepcopy(self.matr)
                                copie_matr[i][j] = '.'
                                copie_matr[elem[0]][elem[1]] = jucator
                                if self.contineLinCol(elem[0],elem[1],copie_matr) == False:
                                    l_mutari.append(Joc(copie_matr))
                                else:  # daca elem mutat a creat o linie full (trebuie stearsa o piesa)
                                    ceva = self.stergeElement(copie_matr,self.jucator_opus(jucator))
                                    for matrice in ceva:
                                        l_mutari.append(Joc(matrice))


        elif self.etapa == 2 and self.nrPiese(jucator) <= 3:
            l_mutari = []
            for i in range(self.lungime):
                for j in range(self.lungime):
                    if self.matr[i][j] == jucator:
                        listaPoz = self.locLiber()
                        for elem in listaPoz:
                            copie_matr = copy.deepcopy(self.matr)
                            copie_matr[i][j] = '.'
                            copie_matr[elem[0]][elem[1]] = jucator
                            if self.contineLinCol(elem[0], elem[1], copie_matr) == False:
                                l_mutari.append(Joc(copie_matr))
                            else:  # daca elem mutat a creat o linie full (trebuie stearsa o piesa)
                                ceva = self.stergeElement(copie_matr, self.jucator_opus(jucator))
                                for matrice in ceva:
                                    l_mutari.append(Joc(matrice))

        return l_mutari
        # . - - . - - .
        # | . - . - . |
        # | | . . . | |
        # . . . _ . . .
        # | | . . . | |
        # | . - . - . |
        # . - - . - - .



    def nrPiese(self,jucator):  # jucator = simbolul jucatorului care muta
        nr = 0
        for i in range(self.lungime):
            for j in range(self.lungime):
                if self.matr[i][j] == jucator:
                    nr += 1
        return nr


    def linieDeschisa(self, l, jucator):
        jo = self.jucator_opus(jucator)
        if not jo in self.matr[l]:
            return 1
        return 0
    def cololanaDeschisa(self, c, jucator):
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

    def estimeazaScor2(self,adancime):   #?
        tFinal = self.final()
        if tFinal == self.__class__.JMAX:  # self.__class__ referinta catre clasa instantei
            return (99 + adancime)
        elif tFinal == self.__class__.JMIN:
            return (-99 - adancime)
        elif tFinal == 'remiza':
            return 0
        else:
            return (self.linColDeschise(self.__class__.JMAX) - self.linColDeschise(self.__class__.JMIN))

    def estimeazaScor(self,adancime):   #?
        tFinal = self.final()
        if tFinal == self.__class__.JMAX:  # self.__class__ referinta catre clasa instantei
            return (9999 + adancime)
        elif tFinal == self.__class__.JMIN:
            return (-9999 - adancime)
        elif tFinal == 'remiza':
            return 0
        else:
            if self.etapa == 2:
                return self.nrPiese(self.__class__.JMAX) - self.nrPiese(self.__class__.JMIN)
            else:
                return self.nrPiese(self.__class__.JMAX) - self.nrPiese(self.__class__.JMIN)

    @classmethod
    def initializeaza(cls):
        cls.noduri = [
        (0, 0),#0
        (0, 3),#1
        (0, 6),#2
        (3, 6),#3
        (6, 6),#4
        (6, 3),#5
        (6, 0),#6
        (3, 0),#7
        (1, 1),#8
        (1, 3),#9
        (1, 5),#10
        (3, 5),#11
        (5, 5),#12
        (5, 3),#13
        (5, 1),#14
        (3, 1),#15
        (2, 2),#16
        (2, 3),#17
        (2, 4),#18
        (3, 4),#19
        (4, 4),#20
        (4, 3),#21
        (4, 2),#22
        (3, 2) #23
        ]

        cls.muchii =[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 0),
              (8, 10), (12, 10), (12, 14), (14, 8),
              (16, 18), (18, 20), (20, 22), (22, 16),
              (1, 17), (7, 23), (3, 19), (5, 21)]

        cls.piesaAlba = pygame.image.load('piesaAlba.png')
        diametruPiesa = 2 * cls.razaPiesa
        cls.piesaAlba = pygame.transform.scale(cls.piesaAlba, (diametruPiesa, diametruPiesa))
        cls.piesaNeagra = pygame.image.load('piesaNeagra.png')
        cls.piesaNeagra = pygame.transform.scale(cls.piesaNeagra, (diametruPiesa, diametruPiesa))
        cls.piesaSelectata = pygame.image.load('piesaRosie.png')
        cls.piesaSelectata = pygame.transform.scale(cls.piesaSelectata, (diametruPiesa, diametruPiesa))
        cls.nodPiesaSelectata = False
        cls.coordonateNoduri = [[cls.translatie + cls.scalare * x for x in nod] for nod in cls.noduri]
        cls.pieseAlbe = []
        cls.nodPiesaSelectata = None
        cls.pieseNegre = []

    def locatiePiese(self, jucator):
        lReala = []
        lInvers = []
        for i in range(self.lungime):
            for j in range(self.lungime):
                if self.matr[i][j] == jucator:
                    lReala.append([i,j])
                    lInvers.append([j,i])
        return lReala, lInvers

    def deseneazaEcranJoc(self,ecran):
        ecran.fill(culoareEcran)
        for nod in self.coordonateNoduri:
            pygame.draw.circle(surface=ecran, color=culoareLinii, center=nod, radius=self.razaPct,
                               width=0)  # width=0 face un cerc plin

        for muchie in self.muchii:
            p0 = self.coordonateNoduri[muchie[0]]
            p1 = self.coordonateNoduri[muchie[1]]
            pygame.draw.line(surface=ecran, color=culoareLinii, start_pos=p0, end_pos=p1, width=5)
        for nod in self.pieseAlbe:
            ecran.blit(self.piesaAlba, (nod[0] - self.razaPiesa, nod[1] - self.razaPiesa))
        for nod in self.pieseNegre:
            ecran.blit(self.piesaNeagra, (nod[0] - self.razaPiesa, nod[1] - self.razaPiesa))
        if self.nodPiesaSelectata:
            ecran.blit(self.piesaSelectata, (self.nodPiesaSelectata[0] - self.razaPiesa, self.nodPiesaSelectata[1] - self.razaPiesa))
        pygame.display.update()

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


def alpha_beta(alpha, beta, stare):
    if stare.adancime == 0 or stare.tablaJoc.final():
        stare.estimare = stare.tablaJoc.estimeazaScor(stare.adancime)
        return stare

    if alpha > beta:
        return stare  # este intr-un interval invalid deci nu o mai procesez

    stare.mutariPosibile = stare.mutari()

    if stare.jucatorCurent == Joc.JMAX:
        estimare_curenta = float('-inf')  # in aceasta variabila calculam maximul

        for mutare in stare.mutariPosibile:
            # calculeaza estimarea pentru starea noua, realizand subarborele
            stare_noua = alpha_beta(alpha, beta, mutare)  # aici construim subarborele pentru stare_noua

            if (estimare_curenta < stare_noua.estimare):
                stare.stareAleasa = stare_noua
                estimare_curenta = stare_noua.estimare
            if (alpha < stare_noua.estimare):
                alpha = stare_noua.estimare
                if alpha >= beta:  # interval invalid
                    break

    elif stare.jucatorCurent == Joc.JMIN:
        estimare_curenta = float('inf')
        # completati cu rationament similar pe cazul stare.j_curent==Joc.JMAX
        for mutare in stare.mutariPosibile:
            # calculeaza estimarea
            stare_noua = alpha_beta(alpha, beta, mutare)  # aici construim subarborele pentru stare_noua

            if (estimare_curenta > stare_noua.estimare):
                stare.stareAleasa = stare_noua
                estimare_curenta = stare_noua.estimare
            if (beta > stare_noua.estimare):
                beta = stare_noua.estimare
                if alpha >= beta:
                    break

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


def main2():
    raspunsV = False

    while not raspunsV:
        adancimeMax = input("Dificultate: 2,3,4\n ")
        if adancimeMax in ['2', '3','4']:
            raspunsV = True
            adancimeMax = int(adancimeMax)
        else:
            print("Nu ati ales o varianta corecta.")


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
    stareC = Stare(tablaC, 'a', adancimeMax)

    # setari interf grafica
    pygame.init()
    pygame.display.set_caption('9 men`s morris -- Octavian Chiriac')
    # dimensiunea ferestrei in pixeli
    # dim_celula=..
    ecran = pygame.display.set_mode(
        size=(700, 700))  # N *100+ (N-1)*dimensiune_linie_despartitoare (dimensiune_linie_despartitoare=1)
    Joc.initializeaza()

    coordPiesaSel = False
    tablaC.deseneazaEcranJoc(ecran)
    # print(Joc.noduri)
    # print(Joc.pieseAlbe)
    sterge = 0
    var = 0
    var2 = 0
    # nodPiesaSelectata = False
    while True:
        if var2 == True:
            break
        if stareC.tablaJoc.etapa == 1:
            if(stareC.jucatorCurent == Joc.JMIN): #daca e randul tau
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN: #click
                        pos = pygame.mouse.get_pos()
                        # for nod in stareC.tablaJoc.noduri:
                        for idx,nod in enumerate(Joc.coordonateNoduri):
                            if distEuclid(pos, nod) <= Joc.razaPct:

                                # aici teste liste mouse
                                print(nod)

                                if Joc.JMIN == 'a':
                                    pieseCurente = Joc.pieseAlbe
                                    pieseOpus =Joc.pieseNegre

                                else:
                                    pieseCurente = Joc.pieseNegre
                                    pieseOpus = Joc.pieseAlbe

                                if sterge == 0:
                                    if nod not in Joc.pieseAlbe + Joc.pieseNegre:
                                        pieseCurente.append(nod)
                                        # print(nod)
                                        linie = Joc.noduri[idx][1]
                                        coloana = Joc.noduri[idx][0]
                                        stareC.tablaJoc.matr[Joc.noduri[idx][1]][Joc.noduri[idx][0]] = Joc.JMIN
                                        stareC.tablaJoc.deseneazaEcranJoc(ecran)

                                        # stergere de piesa nu inca !!!
                                        if stareC.tablaJoc.contineLinCol(linie, coloana, stareC.tablaJoc.matr):
                                            print("am notat")
                                            sterge = 1
                                        else:
                                            Joc.piesePuseMin += 1
                                            if Joc.piesePuseMin == 9 and Joc.piesePuseMax == 9:
                                                Joc.etapa = 2

                                            # afisarea starii jocului in urma mutarii utilizatorului
                                            print("\nTabla dupa mutarea jucatorului")
                                            print(str(stareC))

                                            # testez daca jocul a ajuns intr-o stare finala
                                            # si afisez un mesaj corespunzator in caz ca da
                                            if (afis_daca_final(stareC)):
                                                break

                                            # S-a realizat o mutare. Schimb jucatorul cu cel opus
                                            stareC.jucatorCurent = Joc.jucator_opus(stareC.jucatorCurent)
                                            break
                                if sterge == 1:

                                    listaOpt = []
                                    for i in range(7):
                                        for j in range(7):
                                            if stareC.tablaJoc.matr[i][j] == Joc.JMAX and not stareC.tablaJoc.contineLinCol(i, j,stareC.tablaJoc.matr):
                                                listaOpt.append([Joc.translatie + Joc.scalare * j, Joc.translatie + Joc.scalare * i])
                                    print(listaOpt)
                                    print(Joc.pieseNegre)
                                    if nod in listaOpt:
                                        # print("ghe")
                                        sterge = 0
                                        pieseOpus.remove(nod)
                                        print("amSters" + str(nod))
                                        print(nod)
                                        linie = Joc.noduri[idx][1]
                                        coloana = Joc.noduri[idx][0]
                                        stareC.tablaJoc.matr[Joc.noduri[idx][1]][Joc.noduri[idx][0]] = '.'

                                        # daca s a scapat de o piesa adversa marchez acest lucru la nr total de piese
                                        # stareC.tablaJoc.nrPieseMax = stareC.tablaJoc.nrPieseMax - ( Joc.piesePuseMax - stareC.tablaJoc.nrPiese(Joc.JMAX))
                                        print(str(Joc.nrPieseMax) + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=")
                                        Joc.nrPieseMax = Joc.nrPieseMax - ( Joc.piesePuseMax - stareC.tablaJoc.nrPiese(Joc.JMAX)) + var
                                        var+= 1
                                        print(str(Joc.nrPieseMax) + "======================================================================")
                                        stareC.tablaJoc.deseneazaEcranJoc(ecran)

                                        Joc.piesePuseMin += 1
                                        if Joc.piesePuseMin == 9 and Joc.piesePuseMax == 9:
                                            Joc.etapa = 2

                                        # afisarea starii jocului in urma mutarii utilizatorului
                                        print("\nTabla dupa mutarea jucatorului")
                                        print(str(stareC))

                                        # testez daca jocul a ajuns intr-o stare finala
                                        # si afisez un mesaj corespunzator in caz ca da
                                        if (afis_daca_final(stareC)):
                                            break

                                        print("ghe")
                                        # S-a realizat o mutare. Schimb jucatorul cu cel opus
                                        stareC.jucatorCurent = Joc.jucator_opus(stareC.jucatorCurent)
                                        break



            else:      # randu ai
                print("Acum muta calculatorul cu simbolul", stareC.jucatorCurent)
                # preiau timpul in milisecunde de dinainte de mutare
                t_inainte = int(round(time.time() * 1000))

                # stare actualizata e starea mea curenta in care am setat stare_aleasa (mutarea urmatoare)
                if tip_algoritm == '1':
                    stare_actualizata = min_max(stareC)
                else:  # tip_algoritm==2
                    stare_actualizata = alpha_beta(-500, 500, stareC)
                stareC.tablaJoc = stare_actualizata.stareAleasa.tablaJoc  # aici se face de fapt mutarea !!!

                if Joc.JMAX == 'a':
                    real,fals = stareC.tablaJoc.locatiePiese(Joc.JMAX)
                    Joc.pieseAlbe = []
                    for elem in fals:
                        Joc.pieseAlbe.append([Joc.translatie + Joc.scalare * elem[0],  Joc.translatie + Joc.scalare * elem[1]])
                    real, fals = stareC.tablaJoc.locatiePiese(Joc.JMIN)
                    Joc.pieseNegre = []
                    for elem in fals:
                        Joc.pieseNegre.append(
                            [Joc.translatie + Joc.scalare * elem[0], Joc.translatie + Joc.scalare * elem[1]])
                #
                else:
                    real, fals = stareC.tablaJoc.locatiePiese(Joc.JMAX)
                    Joc.pieseNegre = []
                    for elem in fals:
                        Joc.pieseNegre.append([Joc.translatie + Joc.scalare * elem[0], Joc.translatie + Joc.scalare * elem[1]])
                    real, fals = stareC.tablaJoc.locatiePiese(Joc.JMIN)
                    Joc.pieseAlbe = []
                    for elem in fals:
                        Joc.pieseAlbe.append(
                            [Joc.translatie + Joc.scalare * elem[0], Joc.translatie + Joc.scalare * elem[1]])

                stareC.tablaJoc.deseneazaEcranJoc(ecran)

                print("Tabla dupa mutarea calculatorului")
                print(str(stareC))

                Joc.piesePuseMax += 1
                if Joc.piesePuseMin == 9 and Joc.piesePuseMax == 9:
                    Joc.etapa = 2
                # preiau timpul in milisecunde de dupa mutare
                t_dupa = int(round(time.time() * 1000))
                print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")
                # TO DO 8b

                # daca s a scapat de o piesa adversa marchez acest lucru la nr total de piese
                stareC.tablaJoc.nrPieseMin = stareC.tablaJoc.nrPieseMin - ( Joc.piesePuseMin - stareC.tablaJoc.nrPiese(Joc.JMIN) )

                if (afis_daca_final(stareC)):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                stareC.jucatorCurent = Joc.jucator_opus(stareC.jucatorCurent)



        if stareC.tablaJoc.etapa == 2:
            if (stareC.jucatorCurent == Joc.JMIN):  # daca e randul tau

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    # if var == True:
                    #     var2 = True
                    #     break
                    if event.type == pygame.MOUSEBUTTONDOWN: #click
                        pos = pygame.mouse.get_pos()
                        # for nod in stareC.tablaJoc.noduri:
                        for idx,nod in enumerate(Joc.coordonateNoduri):
                            if distEuclid(pos, nod) <= Joc.razaPct:

                                # aici teste liste mouse
                                print(nod)

                                if Joc.JMIN == 'a':
                                    pieseCurente = Joc.pieseAlbe
                                    pieseOpus =Joc.pieseNegre

                                else:
                                    pieseCurente = Joc.pieseNegre
                                    pieseOpus = Joc.pieseAlbe

                                if sterge == 0:
                                    if nod not in  Joc.pieseAlbe + Joc.pieseNegre:
                                        if Joc.nodPiesaSelectata:
                                            linie = coordPiesaSel[0]
                                            coloana = coordPiesaSel[1]
                                            if stareC.tablaJoc.nrPieseMin > 3:
                                                listaOpt = stareC.tablaJoc.undePotiMuta(linie,coloana)
                                                print("Piesa de pe poz " + str([linie,coloana]) +" are mutarile: " + str(stareC.tablaJoc.undePotiMuta(linie,coloana)))
                                            elif stareC.tablaJoc.nrPieseMin == 3:
                                                listaOpt = stareC.tablaJoc.locLiber()
                                                print("Piesa de pe poz " + str([linie,coloana]) +" are mutarile: " + str(stareC.tablaJoc.locLiber()))

                                            print([Joc.noduri[idx][1], Joc.noduri[idx][0]])
                                            # muti piesa
                                            if ((Joc.noduri[idx][1],Joc.noduri[idx][0]) in listaOpt) or (stareC.tablaJoc.nrPieseMin == 3 and [Joc.noduri[idx][1],Joc.noduri[idx][0]] in listaOpt):
                                                pieseCurente.remove(Joc.nodPiesaSelectata)
                                                pieseCurente.append(nod)

                                                # print(nod)
                                                # linie = Joc.noduri[idx][1]
                                                # coloana = Joc.noduri[idx][0]
                                                stareC.tablaJoc.matr[Joc.noduri[idx][1]][Joc.noduri[idx][0]] = Joc.JMIN
                                                stareC.tablaJoc.matr[linie][coloana] = '.'

                                                Joc.nodPiesaSelectata = False
                                                coordPiesaSel = False
                                                stareC.tablaJoc.deseneazaEcranJoc(ecran)




                                                # stergere de piesa nu inca !!!
                                                if stareC.tablaJoc.contineLinCol(Joc.noduri[idx][1], Joc.noduri[idx][0], stareC.tablaJoc.matr):
                                                    print("am notat")
                                                    sterge = 1
                                                else:


                                                    # afisarea starii jocului in urma mutarii utilizatorului
                                                    print("\nTabla dupa mutarea jucatorului")
                                                    print(str(stareC))

                                                    # testez daca jocul a ajuns intr-o stare finala
                                                    # si afisez un mesaj corespunzator in caz ca da
                                                    if (afis_daca_final(stareC)):
                                                        break

                                                    # S-a realizat o mutare. Schimb jucatorul cu cel opus
                                                    stareC.jucatorCurent = Joc.jucator_opus(stareC.jucatorCurent)
                                                    break
                                    # daca apesi pe o piesa
                                    else:
                                        #apesi pe una din piesele tale
                                        if nod in pieseCurente:
                                            if Joc.nodPiesaSelectata == nod:
                                                Joc.nodPiesaSelectata = False
                                                coordPiesaSel = False
                                            else:
                                                Joc.nodPiesaSelectata = nod
                                                coordPiesaSel = [Joc.noduri[idx][1],Joc.noduri[idx][0]]
                                        stareC.tablaJoc.deseneazaEcranJoc(ecran)

                                if sterge == 1:
                                    print("nr piese negre === " + str(stareC.tablaJoc.nrPieseMax))
                                    # if stareC.tablaJoc.nrPieseMax > 3:
                                    if Joc.nrPieseMax > 3:
                                        listaOpt = []
                                        for i in range(7):
                                            for j in range(7):
                                                if stareC.tablaJoc.matr[i][j] == Joc.JMAX and not stareC.tablaJoc.contineLinCol(i, j,stareC.tablaJoc.matr):
                                                    listaOpt.append([Joc.translatie + Joc.scalare * j, Joc.translatie + Joc.scalare * i])
                                    # elif stareC.tablaJoc.nrPieseMax == 3:
                                    if Joc.nrPieseMax == 3:
                                        listaOpt = []
                                        for i in range(7):
                                            for j in range(7):
                                                if stareC.tablaJoc.matr[i][j] == Joc.JMAX:
                                                    listaOpt.append([Joc.translatie + Joc.scalare * j, Joc.translatie + Joc.scalare * i])
                                    print(listaOpt)
                                    print(Joc.pieseNegre)
                                    if nod in listaOpt:
                                        print("ghe")
                                        sterge = 0
                                        pieseOpus.remove(nod)
                                        print("amSters" + str(nod))
                                        print(nod)
                                        linie = Joc.noduri[idx][1]
                                        coloana = Joc.noduri[idx][0]
                                        stareC.tablaJoc.matr[Joc.noduri[idx][1]][Joc.noduri[idx][0]] = '.'

                                        stareC.tablaJoc.deseneazaEcranJoc(ecran)


                                        # afisarea starii jocului in urma mutarii utilizatorului
                                        print("\nTabla dupa mutarea jucatorului")
                                        print(str(stareC))
                                        # stareC.tablaJoc.nrPieseMax = stareC.tablaJoc.nrPiese(Joc.JMAX)
                                        Joc.nrPieseMax = stareC.tablaJoc.nrPiese(Joc.JMAX)
                                        # testez daca jocul a ajuns intr-o stare finala
                                        # si afisez un mesaj corespunzator in caz ca da
                                        if (afis_daca_final(stareC)):
                                            var = True
                                            break

                                        # print("ghe")
                                        # S-a realizat o mutare. Schimb jucatorul cu cel opus
                                        stareC.jucatorCurent = Joc.jucator_opus(stareC.jucatorCurent)
                                        break


            # . - - . - - .
            # | . - . - . |
            # | | . . . | |
            # . . . _ . . .
            # | | . . . | |
            # | . - . - . |
            # . - - . - - .
            else:  # randu ai
                print("Acum muta calculatorul cu simbolul", stareC.jucatorCurent)
                # preiau timpul in milisecunde de dinainte de mutare
                t_inainte = int(round(time.time() * 1000))

                # stare actualizata e starea mea curenta in care am setat stare_aleasa (mutarea urmatoare)
                if tip_algoritm == '1':
                    stare_actualizata = min_max(stareC)
                else:  # tip_algoritm==2
                    stare_actualizata = alpha_beta(-500, 500, stareC)
                stareC.tablaJoc = stare_actualizata.stareAleasa.tablaJoc  # aici se face de fapt mutarea !!!

                if Joc.JMAX == 'a':
                    real, fals = stareC.tablaJoc.locatiePiese(Joc.JMAX)
                    Joc.pieseAlbe = []
                    for elem in fals:
                        Joc.pieseAlbe.append(
                            [Joc.translatie + Joc.scalare * elem[0], Joc.translatie + Joc.scalare * elem[1]])
                    real, fals = stareC.tablaJoc.locatiePiese(Joc.JMIN)
                    Joc.pieseNegre = []
                    for elem in fals:
                        Joc.pieseNegre.append(
                            [Joc.translatie + Joc.scalare * elem[0], Joc.translatie + Joc.scalare * elem[1]])
                #
                else:
                    real, fals = stareC.tablaJoc.locatiePiese(Joc.JMAX)
                    Joc.pieseNegre = []
                    for elem in fals:
                        Joc.pieseNegre.append(
                            [Joc.translatie + Joc.scalare * elem[0], Joc.translatie + Joc.scalare * elem[1]])
                    real, fals = stareC.tablaJoc.locatiePiese(Joc.JMIN)
                    Joc.pieseAlbe = []
                    for elem in fals:
                        Joc.pieseAlbe.append(
                            [Joc.translatie + Joc.scalare * elem[0], Joc.translatie + Joc.scalare * elem[1]])

                stareC.tablaJoc.deseneazaEcranJoc(ecran)

                print("Tabla dupa mutarea calculatorului")
                print(str(stareC))

                # preiau timpul in milisecunde de dupa mutare
                t_dupa = int(round(time.time() * 1000))
                print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")
                # TO DO 8b

                # daca s a scapat de o piesa adversa marchez acest lucru la nr total de piese
                stareC.tablaJoc.nrPieseMin = stareC.tablaJoc.nrPieseMin - (
                            Joc.piesePuseMin - stareC.tablaJoc.nrPiese(Joc.JMIN))

                if (afis_daca_final(stareC)):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                stareC.jucatorCurent = Joc.jucator_opus(stareC.jucatorCurent)


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

                if stareC.tablaJoc.contineLinCol(linie,coloana,stareC.tablaJoc.matr):
                    listaOpt = []
                    for i in range(7):
                        for j in range(7):
                            if stareC.tablaJoc.matr[i][j] == Joc.JMAX and not stareC.tablaJoc.contineLinCol(i,j,stareC.tablaJoc.matr):
                                listaOpt.append([i,j])
                    print("Alege sa stergi una din piesele adversarului:")
                    print(listaOpt)
                    raspunsV = False
                    while not raspunsV:
                        try:
                            linie2 = int(input("linie="))
                            coloana2 = int(input("coloana="))
                            if linie2 in range(Joc.lungime) and coloana2 in range(Joc.lungime):
                                if stareC.tablaJoc.matr[linie2][coloana2] == Joc.JMAX and not stareC.tablaJoc.contineLinCol(linie2,coloana2,stareC.tablaJoc.matr):
                                    raspunsV = True
                                else:
                                    print("Aici nu se poate pune piesa")
                            else:
                                print("nu sunt coord bune")

                        except ValueError:
                            print("Linia si coloana trebuie sa fie numere intregi")
                    # iesit din while

                    # scot piesa adversa
                    stareC.tablaJoc.matr[linie2][coloana2] = '.'
                    # daca s a scapat de o piesa adversa marchez acest lucru la nr total de piese
                    stareC.tablaJoc.nrPieseMax = stareC.tablaJoc.nrPieseMax - ( Joc.piesePuseMax - stareC.tablaJoc.nrPiese(Joc.JMAX) )

                Joc.piesePuseMin += 1
                if Joc.piesePuseMin == 9 and Joc.piesePuseMax == 9:
                    Joc.etapa = 2

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
                else:  # tip_algoritm==2
                    stare_actualizata = alpha_beta(-500, 500, stareC)
                stareC.tablaJoc = stare_actualizata.stareAleasa.tablaJoc  # aici se face de fapt mutarea !!!
                print("Tabla dupa mutarea calculatorului")
                print(str(stareC))

                Joc.piesePuseMax += 1
                if Joc.piesePuseMin == 9 and Joc.piesePuseMax == 9:
                    Joc.etapa = 2
                # preiau timpul in milisecunde de dupa mutare
                t_dupa = int(round(time.time() * 1000))
                print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")
                # TO DO 8b

                # daca s a scapat de o piesa adversa marchez acest lucru la nr total de piese
                stareC.tablaJoc.nrPieseMin = stareC.tablaJoc.nrPieseMin - ( Joc.piesePuseMin - stareC.tablaJoc.nrPiese(Joc.JMIN) )

                if (afis_daca_final(stareC)):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                stareC.jucatorCurent = Joc.jucator_opus(stareC.jucatorCurent)



        if stareC.tablaJoc.etapa == 2:
            if (stareC.jucatorCurent == Joc.JMIN):  # daca e randul tau
                print("Acum muta utilizatorul cu simbolul", stareC.jucatorCurent)
                print("Alege piesa pe care vrei sa o muti")
                raspunsV = False

                while not raspunsV:
                    try:
                        linie = int(input("linie="))
                        coloana = int(input("coloana="))
                        if linie in range(Joc.lungime) and coloana in range(Joc.lungime):
                            if stareC.tablaJoc.matr[linie][coloana] == Joc.JMIN:
                                if len(stareC.tablaJoc.undePotiMuta(linie,coloana)) > 0:
                                    raspunsV = True
                                else:
                                    print("Piesa nu are mutari posibile")
                            else:
                                print("Aici nu e piesa ta / ")
                        else:
                            print("nu sunt coord bune")

                    except ValueError:
                        print("Linia si coloana trebuie sa fie numere intregi")
                # dupa iesirea din while sigur am valide atat linia cat si coloana
                # gasit piesa de mutat

                ## aici trebuie sa afisezi unde poate fi mutata piesa
                if stareC.tablaJoc.nrPieseMin > 3:
                    print("Piesa de pe poz " + str([linie,coloana]) +" are mutarile: " + str(stareC.tablaJoc.undePotiMuta(linie,coloana)))
                elif stareC.tablaJoc.nrPieseMin == 3:
                    print("Piesa de pe poz " + str([linie,coloana]) +" are mutarile: " + str(stareC.tablaJoc.locLiber()))
                print("Alege unde")
                raspunsV = False
                while not raspunsV:
                    try:
                        linie2 = int(input("linie="))
                        coloana2 = int(input("coloana="))
                        if linie2 in range(Joc.lungime) and coloana2 in range(Joc.lungime):
                            if stareC.tablaJoc.nrPieseMin > 3 and (linie2,coloana2) in stareC.tablaJoc.undePotiMuta(linie,coloana):
                                raspunsV = True
                            elif stareC.tablaJoc.nrPieseMin <= 3 and [linie2,coloana2] in stareC.tablaJoc.locLiber():
                                raspunsV = True
                            else:
                                print("nu e o pozitie valida")
                        else:
                            print("nu sunt coord bune")

                    except ValueError:
                        print("Linia si coloana trebuie sa fie numere intregi")

                stareC.tablaJoc.matr[linie][coloana] = '.'
                stareC.tablaJoc.matr[linie2][coloana2] = Joc.JMIN

                # daca prin mutarea facuta ai facut o linie full
                if stareC.tablaJoc.contineLinCol(linie2,coloana2,stareC.tablaJoc.matr):
                    listaOpt = []
                    for i in range(7):
                        for j in range(7):
                            if stareC.tablaJoc.matr[i][j] == Joc.JMAX and not stareC.tablaJoc.contineLinCol(i,j,stareC.tablaJoc.matr):
                                listaOpt.append([i, j])
                    print("Alege sa stergi una din piesele adversarului:")
                    if stareC.tablaJoc.nrPieseMax > 3:
                        print(listaOpt)
                    elif stareC.tablaJoc.nrPieseMax == 3:
                        listaOpt = []
                        for i in range(7):
                            for j in range(7):
                                if stareC.tablaJoc.matr[i][j] == Joc.JMAX:
                                    listaOpt.append([i, j])
                        print(listaOpt)

                    raspunsV = False
                    while not raspunsV:
                        try:
                            linie2 = int(input("linie="))
                            coloana2 = int(input("coloana="))
                            if linie2 in range(Joc.lungime) and coloana2 in range(Joc.lungime):
                                # if stareC.tablaJoc.matr[linie2][coloana2] == Joc.JMAX and not stareC.tablaJoc.contineLinCol(linie2,coloana2,stareC.tablaJoc.matr):
                                if stareC.tablaJoc.matr[linie2][coloana2] == Joc.JMAX and [linie2,coloana2] in listaOpt:
                                    raspunsV = True
                                else:
                                    print("Aici nu se poate pune piesa")
                            else:
                                print("nu sunt coord bune")

                        except ValueError:
                            print("Linia si coloana trebuie sa fie numere intregi")
                    # iesit din while

                    # eliminarea piesei adversarului
                    stareC.tablaJoc.matr[linie2][coloana2] = '.'

                # afisarea starii jocului in urma mutarii utilizatorului
                print("\nTabla dupa mutarea jucatorului")
                print(str(stareC))

                # testez daca jocul a ajuns intr-o stare finala
                # si afisez un mesaj corespunzator in caz ca da
                stareC.tablaJoc.nrPieseMax = stareC.tablaJoc.nrPiese(Joc.JMAX)
                if (afis_daca_final(stareC)):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                stareC.jucatorCurent = Joc.jucator_opus(stareC.jucatorCurent)

                ## nu stiu dc faci asa nu o sa mint
                # print("Nr piese jucatorii ::    min = " + str(Joc.nrPieseMin) + "::    max = " + str(Joc.nrPieseMax))
                print("Nr piese jucatorii ::    min = " + str(stareC.tablaJoc.nrPieseMin) + "::    max = " + str(stareC.tablaJoc.nrPieseMax))

            # . - - . - - .
            # | . - . - . |
            # | | . . . | |
            # . . . _ . . .
            # | | . . . | |
            # | . - . - . |
            # . - - . - - .
            else:  # randu ai
                print("Acum muta calculatorul cu simbolul", stareC.jucatorCurent)
                # preiau timpul in milisecunde de dinainte de mutare
                t_inainte = int(round(time.time() * 1000))

                # stare actualizata e starea mea curenta in care am setat stare_aleasa (mutarea urmatoare)
                if tip_algoritm == '1':
                    stare_actualizata = min_max(stareC)
                else:  # tip_algoritm==2
                    stare_actualizata = alpha_beta(-500, 500, stareC)
                stareC.tablaJoc = stare_actualizata.stareAleasa.tablaJoc  # aici se face de fapt mutarea !!!
                print("Tabla dupa mutarea calculatorului")
                print(str(stareC))


                # preiau timpul in milisecunde de dupa mutare
                t_dupa = int(round(time.time() * 1000))
                print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")
                # TO DO 8b

                stareC.tablaJoc.nrPieseMin = stareC.tablaJoc.nrPiese(Joc.JMIN)
                if (afis_daca_final(stareC)):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                stareC.jucatorCurent = Joc.jucator_opus(stareC.jucatorCurent)





if __name__ == "__main__":
    # main()
    main2()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    # listaLocuri = [[0, 0], [0, 3], [0, 6], [3, 6], [6, 6], [6, 3], [6, 0], [3, 0], [1, 1], [1, 3], [1, 5], [3, 5],
    #                [5, 5], [5, 3], [5, 1], [3, 1], [2, 2], [2, 3], [2, 4], [3, 4], [4, 4], [4, 3], [4, 2], [3, 2]]
    # print(len(listaLocuri))
    #
    # tabla = Joc()
    # print(tabla)

    # print(tabla.contineLinCol(0,0,tabla.matr))
    #
    #
    #
    # print(tabla)
    # for elem in listaLocuri:
    #     l = tabla.undePotiMuta(elem[0],elem[1])
    #     print(str(elem)+ "  = "+ str(l))
    #
    # l = [[3,2],[2,1],[4,5]]
    # print(set(l))


# . - - . - - .
# | . - . - . |
# | | . . . | |
# . . . _ . . .
# | | . . . | |
# | . - . - . |
# . - - . - - .
