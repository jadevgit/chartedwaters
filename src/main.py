import pandas as pd 
from pathlib import path
import matplotlib.pyplot as plt

def importCSV():
    folder_path = "./src/data"
    return {file_path.stem: pd.read_csv(file_path) for file_path in folder_path.glob("*.csv")}
