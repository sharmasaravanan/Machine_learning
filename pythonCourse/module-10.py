# file handling
# txt, excel, csv

# txt file

inFile = open("MP.txt", "w")
inFile.write("Hey hello how are you\n")
inFile.write("i am good\n")
inFile.write("Thanks for asking\n")
inFile.close()

inFile = open("MP.txt", "a")
inFile.write("bye! take care\n")
inFile.close()

outFile = open("MP.txt", "r")
print(outFile.read())
outFile.close()

outFile = open("MP.txt", "r")
out = outFile.readlines()
print(out[1])
outFile.close()

import os

for file in os.listdir("./"):
    if file.endswith('.txt'):
        inFile = open(file, "a")
        inFile.write("Have a good day!\n")
        inFile.close()
        print(file)

import pandas as pd

excelData = pd.read_excel("./Course Syllabus.xlsx", sheet_name ="Datascience with Python" )
print(excelData.shape)
print(excelData.columns)
print(excelData["Syllabus"])
print(excelData.head(10))

print(excelData[excelData["Duration"] == "3 hours"])
print(excelData[excelData["Duration"].isin(["0.5 hours","3 hours"])])

import pandas as pd

csvData = pd.read_csv("./Advertising.csv" )
print(csvData.shape)
print(csvData.columns)
print(csvData.head(10))
print(csvData[csvData["TV"] >= 150.0])
print(csvData.iloc[5, :])
print(csvData.iloc[5, 1])

import pandas as pd
print(pd.read_clipboard())


import pandas as pd

data = {}
data["Fruits"] = ['Apples','Bananas','Cherries','Dates','Oranges','papaya','kiwi']
data["Veg"] = ['carrot','broccoli','asparagus','cauliflower','corn','cucumber','eggplant']
print(data)

df = pd.DataFrame(data)
print(df)
df.to_csv("Mp.csv", index=False)
df.to_excel("mp.xlsx", index=False)
