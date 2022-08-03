import pandas as pd
import csv

df = pd.read_csv("file1.csv")


del df["Movie_Name"]

df.to_csv('PROJECT.csv') 