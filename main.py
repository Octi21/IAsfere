
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

adancimeMax = 3

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
        return False


    def mutari2(self, jucator):  # jucator = simbolul jucatorului care muta
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
    # . - - . - - .
    # | . - . - . |
    # | | . . . | |
    # . . . _ . . .
    # | | . . . | |
    # | . - . - . |
    # . - - . - - .

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
    main()


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


    ## scenariu y


# . - - . - - .
# | . - . - . |
# | | . . . | |
# . . . _ . . .
# | | . . . | |
# | . - . - . |
# . - - . - - .
