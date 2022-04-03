
# from class2 import parcurgeNod, Graph, verifFile


import time
# import copy
# import itertools
# import os
# import sys
# import math


fileTrimisLaClass2 = "file3.txt"
from class2 import *

# if verifFile("file2.txt"):
#     gr2 = Graph("file2.txt")
if verifFile(numeFile):
    gr2 = Graph(numeFile)
    parcurgeNod.gr = gr2
    # nod = parcurgeNod(1,gr.start,None,gr.sfere,None,0,0)
    # print(nod.sfere)
    # print(str(nod))

    # print(gr.genereazaSuccesori2(nod))
    # for nod2 in gr.genereazaSuccesori2(nod):
    #     print(str(nod2))

    def check_time(start, limit):
        actual = time.time()
        if actual - start > limit:
            return True
        return False


    def a_star(gr2, nrSolutiiCautate, tip_euristica, timeout):
        # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
        c = [parcurgeNod(1,gr2.start,None,gr2.sfere,None,0,0)]
        t1 = time.time()

        while len(c) > 0:
            if check_time(t1,timeout):
                print("depasit timp")
                return

            print("DIMENSIUNEA COZII = " + str(len(c)))
            # print(str(c))
            nodCurent = c.pop(0)
            if len(c) % 1023 == 1:
                print(str(nodCurent))

            if gr2.testeazaScop(nodCurent):
                print("Solutie: ")
                nodCurent.afisDrum()
                print("\n----------------\n")
                # input()
                nrSolutiiCautate -= 1
                if nrSolutiiCautate == 0:
                    return
            lSuccesori = gr2.genereazaSuccesori2(nodCurent, tip_euristica=tip_euristica)
            for s in lSuccesori:
                i = 0
                gasit_loc = False
                for i in range(len(c)):
                    # diferenta fata de UCS e ca ordonez dupa f
                    if c[i].f >= s.f:
                        gasit_loc = True
                        break
                if gasit_loc:
                    c.insert(i, s)
                else:
                    c.append(s)

    #euristica_banala
    #admisibila1

    # a_star(gr2, nrSolutiiCautate=1, tip_euristica="admisibila2",timeout = 10)



