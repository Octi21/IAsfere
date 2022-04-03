
import time
import copy
import itertools
import os
import sys
import math

def fa1():
    for i in range(len(sys.argv)):
        print("Argumentul {} are valoarea {} si tipul de date {}".format(i, sys.argv[i], type(sys.argv[i])))
    listaFisiereInput = os.listdir(sys.argv[1])
    listaFisiereOutput = os.listdir(sys.argv[2])
    nrSol = sys.argv[3]
    timeout = sys.argv[4]
    print(listaFisiereInput)
    print(listaFisiereOutput)
    print(nrSol)
    print(timeout)


a = 1
if a == 1:
    from a_star import *

    # euristica_banala
    # admisibila1
    # euristica_neadmisibila
    t0 = time.time()
    a_star(gr2, nrSolutiiCautate=2, tip_euristica="euristica_neadmisibila",timeout = 10)
    t1 = time.time()
    print("Alg a durat = " + str(t1 - t0))


else:
    print("nu ai ales nmc")


# python main.py folder_input folder_output 4 10
# fa1()