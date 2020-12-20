### style 3 (marco)
#prendo i numeri in input e li metto in una matrice dove o c'e' 0 o c'e 1 se esiste il numero 
#corrispondente all'indice
#per ciascun numero calcolo complemento a 2020
#vado nella matrice alla posizione (numero). Se c'e' 0 provo col successivo, se c'e' 1 la 
#soluzione e' l'indice.
#calcolo indice * complemento-a-2020
#

#import numpy as np

#read the file
with open("day1-data.txt") as f:
    l = [
        int(line)
        for line in f.read().splitlines()
    ]

#trovo il massimo nella lista
maxValueInList = max(l)
#trovo il numero di elementi in L
numElementInLn = len(l)

print('elementi in l: ',numElementInLn,' maxValueInList: ',maxValueInList)

#creo la matrice e inizializzo a 0

arr=[]
arr = [0] * (2021)

iterCount = 0

#put 1 in arr[i] if number exists
for i in range(numElementInLn):
    arr[l[i]]=1
    iterCount +=1

#per ciascun numero calcolo complemento a 2020
#vado nella matrice alla posizione (numero). Se c'e' 0 provo col successivo, se c'e' 1 la 
#soluzione e' l'indice.   

for i in range(numElementInLn):
    iterCount +=1
    complementoA2020 = 2020-l[i]
    
#    print("l[i],complemento: ", l[i],complementoA2020)

    if arr[complementoA2020] == 1:
        print ("The two numbers are: ",l[i],complementoA2020)
        print ("Solution: ", l[i]*complementoA2020," found in ",iterCount," iterations")
    
        break
    

