
import time
import copy
import itertools
import os
import sys
import math
from a_star import fileTrimisLaClass2


class parcurgeNod:
    gr = None      # ob graph

    def __init__(self, id, info, matSchimbari, sfere, parent, cost=0, h=0):
        self.id = id
        self.info = info
        self.sfere = sfere      # lista de liste de pozitii bile
        self.parent = parent
        self.g = cost
        self.h = h
        self.f = self.h + self.g

        self.info2 = copy.deepcopy(gr.matGraf)
        for poz in self.sfere:
            if poz in gr.scopuri:
                self.info2[poz[0]][poz[1]] = "%"
            else:
                self.info2[poz[0]][poz[1]] = "@"
        if id == 1:
            self.matSchimbari = gr.marModif
        else:
            self.matSchimbari = matSchimbari

        # for linie in self.matSchimbari:
        #     print(linie)



    def obtineDrum(self):
        l = [self]
        nodCurent = self
        while nodCurent.parent is not None:
            nodCurent = nodCurent.parent
            l.insert(0,nodCurent)
        return l

    def afisDrum(self):
        l = self.obtineDrum()
        for nod in l:
            print(str(nod))
        return len(l)

    def contineInDrum(self, sfereNodNou):
        nodDrum = self
        while nodDrum is not None:
            if (sfereNodNou == nodDrum.sfere):
                return True
            nodDrum = nodDrum.parent

        return False

    def __repr__(self):
        sir = ""
        sir = sir + str(self.sfere)
        return sir

    def __str__(self):
        sir = str(self.id) + ")\n"
        if self.parent != None:
            mat1 = self.matSchimbari
            mat2 = self.parent.matSchimbari
            l = len(mat1)
            for i in range(l):
                for j in range(l):
                    if mat1[i][j] != mat2[i][j]:
                        sir += "turnul (" + str(i) +","+str(j)+") " + "a scazut cu " + str(mat1[i][j] - mat2[i][j] ) + "\n"
            sir += 'afis noduri modif\n'
        sir += "cost:" +str(self.g) + "\nMat turn: \n"
        for linie in self.info:
            for elem in linie:
                sir += str(elem) + " "
            sir += "\n"
        sir += "Mat sfere: \n"
        for linie in self.info2:
            for elem in linie:
                sir += str(elem) + " "
            sir += "\n"
        return sir

    def __gt__(self, other):
        if self.f == other.f:
            return self.g < other.g
        return self.f > other.f


class Graph:

    def __init__(self,numeFisier):
        f = open(numeFisier,'r')
        primaLin = f.readline()
        l = primaLin.split()
        self.k = int(l[0])
        self.distMax = int(l[1])

        self.start = []
        self.matGraf = []
        self.marModif = []

        self.sfere = []
        self.scopuri = []
        rest = f.read()
        l = rest.split("sfere\n")
        l2 = l[0].strip().split("\n")
        for linie in l2:
            lMat = []
            lMat2 = []
            lMat3 = []
            for elem in linie.split():
                lMat.append(int(elem))
                lMat2.append('.')
                lMat3.append(0)
            self.start.append(lMat)
            self.matGraf.append(lMat2)
            self.marModif.append(lMat3)


        # print("prima lin a fis = " + str(self.k) +" " +str(self.distMax))
        # print(str(self.start))
        l = l[1].split("\niesiri\n")
        for rand in l[0].split("\n"):
            lMat = []
            for elem in rand.split():
                lMat.append(int(elem))
            self.sfere.append(lMat)

        # print(str(self.sfere))

        for rand in l[1].strip().split("\n"):
            lMat = []
            for elem in rand.split():
                lMat.append(int(elem))
            self.scopuri.append(lMat)


        for iesire in self.scopuri:
            self.matGraf[iesire[0]][iesire[1]] = '#'
        # for rand in self.matGraf:
        #     print(rand)
        # print(self.scopuri)

    def testeazaScop(self, nodCurent):
        locSfere = nodCurent.sfere
        for loc in locSfere:
            if locSfere.count(loc) > 1:
                return False
            if self.scopuri.count(loc) == 0:
                return False
        return True


    def genereazaSuccesori2(self, nodCurent, tip_euristica="euristica banala"):
        listaSuccesori = []
        pozSf = nodCurent.sfere
        lcomb = []
        for poz in pozSf:
            for i in range(poz[0] - self.distMax, poz[0] + self.distMax + 1):
                for j in range(poz[1] - self.distMax, poz[1] + self.distMax + 1):
                    if abs(i - poz[0]) + abs(j - poz[1]) <= self.distMax and [i,j] != poz and i >= 0 and \
                            i<len(self.start) and j<len(self.start) and j >=0:     # poz turnurilor pt dist manhattan
                        lcomb.append([i,j])

        # listaSuccesori = list(map(list,itertools.combinations(listaSuccesori,math.ceil(len(pozSf)*2/3))))
        lcomb = list(itertools.combinations(lcomb, math.ceil(len(pozSf) * 2 / 3)))                  # generarea de combinari

        def bilaApoape(turn,lPozsfere):
            pozM = 10000
            poz = turn
            for elem in lPozsfere:
                if abs(turn[0] - elem[0]) + abs(turn[1] - elem[1]) < pozM:
                    pozM = abs(turn[0] - elem[0]) + abs(turn[1] - elem[1])
                    poz = elem
            return poz

        def genPoz(coord,maxx):
            l = []
            if coord[0] - 1 >= 0:
                l.append([coord[0] - 1, coord[1]])
            if coord[1] + 1 < maxx:
                l.append([coord[0], coord[1] + 1])
            if coord[0] + 1 < maxx:
                l.append([coord[0] + 1, coord[1]])
            if coord[1] - 1 >= 0:
                l.append([coord[0], coord[1] - 1])

            return l

        # print(bilaApoape([3, 2], self.sfere))

        lPos = []                   # pentru toate bilele toate posibilitatile
        for elem in nodCurent.sfere:
            ghe = genPoz(elem,len(self.start))
            lPos.append(ghe)
        # print(lPos)


        for li in lcomb:                                                # li = toate posibilitatie de liste de modif de turnuri
            copieM = copy.deepcopy(nodCurent.info)
            copieD = copy.deepcopy(nodCurent.matSchimbari)
            ok = 1
            for elem in li:                                             # aici modif matricea si retin schimarile turnurilor elem = turnurile din li
                if elem in nodCurent.sfere:         # pentru a nu afecta marimea unui turn pe care se afla o bila
                    ok = 0
                    # print("ghe")
                    continue
                mainTurn = bilaApoape(elem,nodCurent.sfere)                  # pt a gasi turnul care a generat aceasta schimbare
                # print(mainTurn)
                distM = abs(mainTurn[0] - elem[0]) + abs(mainTurn[1] - elem[1])
                val = copieM[elem[0]][elem[1]] - copieM[mainTurn[0]][mainTurn[1]]
                if(val > 0):
                    if(val + distM < self.k):
                        copieM[elem[0]][elem[1]] -= val + distM
                        copieD[elem[0]][elem[1]] += val + distM
                        # trebuie retinuta schimbarea in cv dict pt costul unei eventuale muttari
                    else:
                        copieM[elem[0]][elem[1]] -= self.k
                        copieD[elem[0]][elem[1]] += self.k
                else:
                    copieM[elem[0]][elem[1]] -= 1
                    copieD[elem[0]][elem[1]] += 1
            if ok == 0:
                # print("ghe2")
                continue
            # am modif matricea aici trebuie sa aplic mutarile pt matricea schimbata
            # am retinut cu cat a fost modiif un turn in matricea modifD


            pozSfereNoi = []                        # unde vor fi sferele la finalul mutarii
            costMutari = 0                          # cat costa mutarile

            def bestAleg(poz,lPoz):                             # functie care returneaza unde se va muta bila
                maxx = 0
                retin = poz
                for elem in lPoz:
                    # if elem[0] >= 0 and elem[0] < len(self.start) and elem[1] >= 0 and elem[1] < len(self.start):
                    if copieM[elem[0]][elem[1]] < copieM[poz[0]][poz[1]] and copieM[elem[0]][elem[1]] > maxx:
                            maxx = copieM[elem[0]][elem[1]]
                            retin = elem
                return retin

            # for linie in copieM:
            #     print(linie)
            # for linie in copieD:
            #     print(linie)w


            for i in range(len(self.sfere)):                            # generez mutarea sferelor
                # print(self.sfere[i])
                # print(lPos[i])
                if nodCurent.sfere[i] not in self.scopuri:                     # mut o bila doar daca nu e deja pe poarta
                    nouaCoordBi = bestAleg(nodCurent.sfere[i],lPos[i])
                    pozSfereNoi.append(nouaCoordBi)
                    costMutari += copieD[nouaCoordBi[0]][nouaCoordBi[1]] **2
                else:
                    pozSfereNoi.append(nodCurent.sfere[i])
                    # print("O bila deja a iesit")

                # print("Noua Poz pt bila " + str(i+1) + " = " + str(nouaCoordBi))

            ok = 1                              # pentru a sari variantele in care bilele sunt pe margine si nu sunt stari fin / 2b ac turn
            for poz in pozSfereNoi:
                if pozSfereNoi.count(poz) > 1:
                    ok = 0
                    break
                if poz not in self.scopuri:
                    if poz[0] == 0 or poz[0] == len(self.start) or poz[1] == 0 or poz[1] == len(self.start):
                        ok = 0
                        break
            if ok == 0:
                continue

            # acm aici trebuie sa generezi ob de tip parcurgeNod  si sa adaugi in succesori

            if pozSfereNoi != nodCurent.sfere and not nodCurent.contineInDrum(list(pozSfereNoi)):
                # def __init__(self, id, info, matSchimbari, sfere, parent, cost=0, h=0):
                listaSuccesori.append(parcurgeNod(nodCurent.id + 1, copieM, copieD, list(pozSfereNoi), nodCurent,
                                                  cost=nodCurent.g + costMutari, h=self.calculeaza_h(list(pozSfereNoi), copieM, tip_euristica)))

            # print("NOUL POZ SFERE = " + str(pozSfereNoi))

            # print(li)
        return listaSuccesori




    def calculeaza_h(self, pozitieSfere, matTurnuri, tip_euristica="euristica_banala"):
        if tip_euristica == "euristica_banala":
            for infoBila in pozitieSfere:
                if self.scopuri.count(infoBila):
                    return 1  # se pune costul minim pe o mutare
            return 0
        elif tip_euristica == "admisibila1":
            h = []
            for infoBila in pozitieSfere:
                min = 1000
                for poarta in self.scopuri:
                    dist = abs(poarta[0] - infoBila[0]) + abs(poarta[1] - infoBila[1])
                    if dist < min:
                        min = dist
                h.append(min)
            return max(h)
        elif tip_euristica == "admisibila2":
            h = []
            for infoBila in pozitieSfere:
                min = 1000
                cost = 0
                for poarta in self.scopuri:
                    dist = abs(poarta[0] - infoBila[0]) + abs(poarta[1] - infoBila[1])
                    if dist < min:
                        min = dist
                        cost = matTurnuri[poarta[0]][poarta[1]] - matTurnuri[infoBila[0]][infoBila[1]]
                        if cost < 0:
                            cost = 0
                h.append(min+cost)
            return max(h)
        elif tip_euristica == "euristica_neadmisibila":
            h = 0
            for infoBila in pozitieSfere:
                min = 1000
                for poarta in self.scopuri:
                    dist = abs(poarta[0] - infoBila[0]) + abs(poarta[1] - infoBila[1])
                    if dist < min:
                        min = dist
                h += min
            return h * h * h


# numeFile = input("File-ul Ales = ")
numeFile = fileTrimisLaClass2
gr = Graph(numeFile)
parcurgeNod.gr = gr




def verifFile(numeFile):
    f = open(numeFile,"r")
    primaLinie = f.readline()
    primaLinie = primaLinie.split()
    # print(primaLinie)

    if len(primaLinie) != 2:
        print("Nu respecta prima linie")
        return False

    sir = f.read()

    if sir.count("sfere") == 0 or sir.count("iesiri") == 0:
        print(sir.count("sfere"))
        print(sir.count("iesiri"))
        print("nu apare separator sfere sau iesiri")
        return False

    sir = sir.split("\nsfere\n")
    # print(sir[0])
    # print(sir[1])

    matrice  = sir[0]
    matrice = matrice.split("\n")
    nrL = len(matrice)
    # print(nrL)
    for linie in matrice:
        linie = linie.split()
        # print(linie)
        if len(linie) != nrL:
            print("Insuficiente elem pe linie")
            return False
        for elem in linie:
            if not elem.isnumeric():
                print("Nu e numar")
                return False

    sir1 = sir[1].split("\niesiri\n")
    # print(sir1[0])
    # print(sir1[1])
    sfere  = sir1[0].split("\n")
    for rand in sfere:
        rand = rand.split()
        if len(rand) != 2:
            print("coord gresite sfere")
            return False

        for elem in rand:
            # print(elem)
            if not elem.isnumeric():
                print("Nu e numar")
                return False
            if elem == '0' or elem == str(nrL - 1):
                print("e pe margine din input o bila")
                return False

    iesire = sir1[1].split("\n")
    for rand in iesire:
        rand  = rand.split()
        if len(rand) != 2:
            print("coord gresite iesire")
            return False
        # print(rand)
        margine = 0
        for elem in rand:
            if not elem.isnumeric():
                print("Nu e numar")
                return False
            if elem == '0' or elem == str(nrL - 1):
                margine += 1
        if margine == 0:
            print("poarta nu e pe marginea matricei")
            return False

    print()
    return True


# print(verifFile("file.txt"))


# if verifFile("file3.txt"):
#     gr = Graph("file3.txt")
#     parcurgeNod.gr = gr
#     # nod = parcurgeNod(1,gr.start,None,gr.sfere,None,0,0)
#     # print(nod.sfere)
#     # print(str(nod))
#
#     # print(gr.genereazaSuccesori2(nod))
#     # for nod2 in gr.genereazaSuccesori2(nod):
#     #     print(str(nod2))
#
#
#     def a_star(gr, nrSolutiiCautate, tip_euristica):
#         # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
#         c = [parcurgeNod(1,gr.start,None,gr.sfere,None,0,0)]
#
#         while len(c) > 0:
#             print("DIMENSIUNEA COZII = " + str(len(c)))
#             # print(str(c))
#             nodCurent = c.pop(0)
#             if len(c) % 1023 == 1:
#                 print(str(nodCurent))
#
#             if gr.testeazaScop(nodCurent):
#                 print("Solutie: ")
#                 nodCurent.afisDrum()
#                 print("\n----------------\n")
#                 # input()
#                 nrSolutiiCautate -= 1
#                 if nrSolutiiCautate == 0:
#                     return
#             lSuccesori = gr.genereazaSuccesori2(nodCurent, tip_euristica=tip_euristica)
#             for s in lSuccesori:
#                 i = 0
#                 gasit_loc = False
#                 for i in range(len(c)):
#                     # diferenta fata de UCS e ca ordonez dupa f
#                     if c[i].f >= s.f:
#                         gasit_loc = True
#                         break
#                 if gasit_loc:
#                     c.insert(i, s)
#                 else:
#                     c.append(s)
#
#     #euristica banala
#     #admisibila1
#     t0 = time.time()
#     # a_star(gr, nrSolutiiCautate=1, tip_euristica="admisibila2")
#     t1 = time.time()
#
#     print("Alg a durat = " + str(t1 - t0))





