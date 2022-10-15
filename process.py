import csv
import pandas as pd

dataset = []

df = pd.read_csv("dwarf_stars.csv")
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]
df = df[df['Distance'].notna()]
df = df[df['Star_Names'].notna()]

df.to_csv('main.csv')

with open("main.csv",'r') as f:
    csv_reader = csv.reader(f)

    i = 0
    for row in csv_reader:
        if(i>0):
            dataset.append([row[0],row[1],row[2],float(row[3])*0.000954588,float(row[4])*0.102763])
        else:
            dataset.append(row)

        i+=1

with open("merged_dataset.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(dataset[0])
    csv_writer.writerows(dataset[1:])