import pandas as pd

datafile = pd.read_csv("datatest.txt", delimiter="\t")
datafile.to_csv("datatest.csv", index = None)
