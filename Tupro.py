import csv
import operator
import math

DataTrain = []
DataTest = []

with open("TrainsetTugas1ML.csv","r") as myFile:
    myFile = csv.reader(myFile, delimiter=',')
    line_count = 0
    for line in myFile:
        if line_count == 0:
            line_count += 1
        else:
            DataTrain.append(line)

with open('TestsetTugas1ML.csv') as csv_file:
    iFile = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for line in iFile:
        if line_count == 0:
            line_count += 1
        else:
            DataTest.append(line)

#SUBTABEL 1
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
i=0
j=0
g=0
h=0
while j < len(DataTrain):
    if (DataTrain[j][8] == ">50K"):
        g += 1
    elif DataTrain[j][8] == "<=50K":
        h += 1
    j += 1

while i < len(DataTrain):
    if (DataTrain[i][1] == "young"):
        if (DataTrain[i][8] == ">50K"):
            a1 = a1+1
    elif (DataTrain[i][1] == "young"):
        if (DataTrain[i][8] == "<=50K"):
            a2 = a2+1
    if (DataTrain[i][1] == "adult"):
        if (DataTrain[i][8] == ">50K"):
            a3 = a3+1
    elif (DataTrain[i][1] == "adult"):
        if (DataTrain[i][8] == "<=50K"):
            a4 = a4+1
    if (DataTrain[i][1] == "old"):
        if (DataTrain[i][8] == ">50K"):
            a5 = a5+1
    elif (DataTrain[i][1] == "old"):
        if (DataTrain[i][8] == "<=50K"):
            a6 = a6+1
    i += 1


persena1 = a1 / g
persena2 = a2 / h
persena3 = a3 / g
persena4 = a4 / h
persena5 = a5 / g
persena6 = a6 / h

#SUBTABEL2
b1=0
b2=0
b3=0
b4=0
b5=0
b6=0
i=0
while i < len(DataTrain):
    if (DataTrain[i][2] == "Private"):
        if (DataTrain[i][8] == ">50K"):
            b1 = b1+1
    elif (DataTrain[i][2] == "Private"):
        if (DataTrain[i][8] == "<=50K"):
            b2 = b2+1
    if (DataTrain[i][2] == "Local-gov"):
        if (DataTrain[i][8] == ">50K"):
            b3 = b3+1
    elif (DataTrain[i][2] == "Local-gov"):
        if (DataTrain[i][8] == "<=50K"):
            b4 = b4+1
    if (DataTrain[i][2] == "Self-emp-not-inc") and (DataTrain[i][8] == ">50K"):
        b5 = b5+1
    elif (DataTrain[i][2] == "Self-emp-not-inc") and (DataTrain[i][8] == "<=50K"):
        b6 = b6+1
    i += 1

persenb1 = b1/g
persenb2 = b2/h
persenb3 = b3/g
persenb4 = b4/h
persenb5 = b5/g
persenb6 = b6/h

#SUBTABEL3
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
i=0
while i < len(DataTrain):
    if (DataTrain[i][3] == "Bachelors") and (DataTrain[i][8] == ">50K"):
        c1 = c1+1
    elif (DataTrain[i][3] == "Bachelors") and (DataTrain[i][8] == "<=50K"):
        c2 = c2+1
    if (DataTrain[i][3] == "Some-college") and (DataTrain[i][8] == ">50K"):
        c3 = c3+1
    elif (DataTrain[i][3] == "Some-college") and (DataTrain[i][8] == "<=50K"):
        c4 = c4+1
    if (DataTrain[i][3] == "HS-grad") and (DataTrain[i][8] == ">50K"):
        c5 = c5+1
    elif (DataTrain[i][3] == "HS-grad") and (DataTrain[i][8] == "<=50K"):
        c6 = c6+1
    i += 1


persenc1 = c1/g
persenc2 = c2/h
persenc3 = c3/g
persenc4 = c4/h
persenc5 = c5/g
persenc6 = c6/h

#SUBTABEL4
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
d6 = 0
d7 = 0
i=0
while i < len(DataTrain):
    if (DataTrain[i][4] == "Married-civ-spouse") and (DataTrain[i][8] == ">50K"):
        d1 = d1+1
    elif (DataTrain[i][4] == "Married-civ-spouse") and (DataTrain[i][8] == "<=50K"):
        d2 = d2+1
    if (DataTrain[i][4] == "Never-married") and (DataTrain[i][8] == ">50K"):
        d3 = d3+1
    elif (DataTrain[i][4] == "Never-married") and (DataTrain[i][8] == "<=50K"):
        d4 = d4+1
    if (DataTrain[i][4] == "Divorced") and (DataTrain[i][8] == ">50K"):
        d5 = d5+1
    elif (DataTrain[i][4] == "Divorced") and (DataTrain[i][8] == "<=50K"):
        d6 = d6+1
    i += 1

persend1 = d1/g
persend2 = d2/h
persend3 = d3/g
persend4 = d4/h
persend5 = d5/g
persend6 = d6/h

#SUBTABEL5
e1 = 0
e2 = 0
e3 = 0
e4 = 0
e5 = 0
e6 = 0

i=0
while i < len(DataTrain):
    if (DataTrain[i][5] == "Exec-managerial") and (DataTrain[i][8] == ">50K"):
        e1 = e1+1
    elif (DataTrain[i][5] == "Exec-managerial") and (DataTrain[i][8] == "<=50K"):
        e2 = e2+1
    if (DataTrain[i][5] == "Prof-specialty") and (DataTrain[i][8] == ">50K"):
        e3 = e3+1
    elif (DataTrain[i][5] == "Prof-specialty") and (DataTrain[i][8] == "<=50K"):
        e4 = e4+1
    if (DataTrain[i][5] == "Craft-repair") and (DataTrain[i][8] == ">50K"):
        e5 = e5+1
    elif (DataTrain[i][5] == "Craft-repair") and (DataTrain[i][8] == "<=50K"):
        e6 = e6+1
    i += 1



persene1 = e1/g
persene2 = e2/h
persene3 = e3/g
persene4 = e4/h
persene5 = e5/g
persene6 = e6/h

#SUBTABEL6
f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
f7 = 0
i=0
while i < len(DataTrain):
    if (DataTrain[6][8] == "Own-child") and (DataTrain[i][8] == ">50K"):
        f1 = f1+1
    elif (DataTrain[6][8] == "Own-child") and (DataTrain[i][8] == "<=50K"):
        f2 = f2+1
    if (DataTrain[6][8] == "Husband") and (DataTrain[i][8] == ">50K"):
        f3 = f3+1
    elif (DataTrain[6][8] == "Husband") and (DataTrain[i][8] == "<=50K"):
        f4 = f4+1
    if (DataTrain[6][8] == "Not-in-family") and (DataTrain[i][8] == ">50K"):
        f5 = f5+1
    elif (DataTrain[6][8] == "Not-in-family") and (DataTrain[i][8] == "<=50K"):
        f6 = f6+1
    i += 1



persenf1 = f1/g
persenf2 = f2/h
persenf3 = f3/g
persenf4 = f4/h
persenf5 = f5/g
persenf6 = f6/h

#SUBTABEL7
h1 = 0
h2 = 0
h3 = 0
h4 = 0
h5 = 0
h6 = 0
i=0
while i < len(DataTrain):
    if (DataTrain[i][7] == "normal") and (DataTrain[i][8] == ">50K"):
        h1 = h1+1
    elif (DataTrain[i][7] == "normal") and (DataTrain[i][8] == "<=50K"):
        h2 = h2+1
    if (DataTrain[i][7] == "low") and (DataTrain[i][8] == ">50K"):
        h3 = h3+1
    elif (DataTrain[i][7] == "low") and (DataTrain[i][8] == "<=50K"):
        h4 = h4+1
    if (DataTrain[i][7] == "many") and (DataTrain[i][8] == ">50K"):
        h5 = h5+1
    elif (DataTrain[i][7] == "many") and (DataTrain[i][8] == "<=50K"):
        h5 = h5+1
    i += 1

persenh1 = h1/g
persenh2 = h2/h
persenh3 = h3/g
persenh4 = h4/h
persenh5 = h5/g
persenh6 = h6/h

income = []
i = 0
while i < (len(DataTest)):
        if DataTest[i][0] == 'young':
            Yes = persena1 * 1
            No = persena2 * 1
        elif DataTest[i][0] == 'adult':
            Yes = persena3 * 1
            No = persena4 * 1
        elif DataTest[i][0] == 'old':
            Yes = persena5 * 1
            No = persena6 * 1
        if DataTest[i][1] == 'Private':
            Yes = persenb1 * Yes
            No = persenb2 * No
        elif DataTest[i][1] == 'Local-gov':
            Yes = persenb3 * Yes
            No = persenb4 * No
        elif DataTest[i][1] == 'Self-emp-not-inc':
            Yes = persenb5 * Yes
            No = persenb6 * No
        if DataTest[i][2] == 'Bachelors':
            Yes = persenc1 * Yes
            No = persenc2 * No
        elif DataTest[i][2] == 'Some-college':
            Yes = persenc3 * Yes
            No = persenc4 * No
        elif DataTest[i][2] == 'HS-grad':
            Yes = persenc5 * Yes
            No = persenc6 * No
        if DataTest[i][3] == 'Married-civ-spouse':
            Yes = persend1 * Yes
            No = persend2 * No
        elif DataTest[i][3] == 'Never-married':
            Yes = persend3 * Yes
            No = persend4 * No
        elif DataTest[i][3] == 'Divorced':
            Yes = persend5 * Yes
            No = persend6 * No
        if DataTest[i][4] == 'Exec-managerial':
            Yes = persene1 * Yes
            No = persene2 * No
        elif DataTest[i][4] == 'Prof-specialty':
            Yes = persene3 * Yes
            No = persene4 * No
        elif DataTest[i][4] == 'Craft-repair':
            Yes = persene5 * Yes
            No = persene6 * No
        if DataTest[i][5] == 'Own-child':
            Yes = persenf1 * Yes
            No = persenf2 * No
        elif DataTest[i][5] == 'Husband':
            Yes = persenf3 * Yes
            No = persenf4 * No
        elif DataTest[i][5] == 'Not-in-family':
            Yes = persenf5 * Yes
            No = persenf6 * No
        if DataTest[i][6] == 'normal':
            Yes = persenh1 * Yes
            No = persenh2 * No
        elif DataTest[i][6] == 'low':
            Yes = persenh3 * Yes
            No = persenh4 * No
        elif DataTest[i][6] == 'many':
            Yes = persenh5 * Yes
            No = persenh6 * No

        if Yes > No:
            income.append('>50K')
        else:
            income.append('<=50K')

        i += 1


with open('TebakanTugas1ML.csv', 'w', newline='') as write:
    writeup = csv.writer(write)
    for i in range(0, len(DataTest)):
        writeup.writerow({income[i]})