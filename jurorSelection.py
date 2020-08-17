import csv
import random
from pathlib import Path

nOfJury = 0
finalJuryList = []
rand = 0
oldRand = []

def createRandomSortedList(num, start = 1, end = 100): 
    arr = [] 
    tmp = random.randint(start, end) 
      
    for x in range(num): 
          
        while tmp in arr: 
            tmp = random.randint(start, end) 
              
        arr.append(tmp) 
          
    arr.sort() 
      
    return arr 
   

def importList():
    base_path = Path(__file__).parent
    file_path = (base_path / "jurorList.txt").resolve()

    with open(file_path) as f:
        lines = f.read().splitlines()

    return lines

def returnJuryList():
    if(input("Is the file 'jurorList.txt' present? (y/n) ") == "y"):
        jurorList = importList();

        nOfJury = int(input("Size of Jury: (1-"+str(len(jurorList))+") "))
        while int(nOfJury) > len(jurorList):
            nOfJury = int(input("Size of Jury: (1-"+str(len(jurorList))+") "))                   

        data = createRandomSortedList(nOfJury, 0, len(jurorList)-1);

        print("")
        print("Jury List: ")
        for i in range(nOfJury):
            #print(str(i)+jurorList[data[i]])
            num = data[i]
            print("Juror no."+str(num+1)+": "+jurorList[num])
            finalJuryList.append(str(num+1)+": "+jurorList[num])

while(input(">>> Create list for jury duty? (y/n) ") == "y"):
    returnJuryList()
    print("")
