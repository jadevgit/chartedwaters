import pandas as pd 
from pathlib import Path
import matplotlib.pyplot as plt

def importCSV():
    folder_path = "./src/data"
    df = {file_path.stem: pd.read_csv(file_path) for file_path in Path(folder_path).glob("*.csv")}
    print("CSVs imported sucessfully! ")
    return df

def checkdata(dfs):
    
    for key, value in dfs.items():
        value.fillna({"Calories": 130}, inplace=True) # Default calories value
        value['Date'] = pd.to_datetime(value['Date'], format='mixed') #DT Correct format check
        value = value.dropna(inplace=True) # N/A Check
    print(dfs)





def main():
    dfs = importCSV()
    clean_dfs = checkdata(dfs)
    


main()