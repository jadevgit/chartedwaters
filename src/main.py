import pandas as pd 
from pathlib import Path

def importCSV():
    folder_path = Path("./src/data")
    csv_files = list(folder_path.glob("*.csv"))
        
    df = {file_path.stem: pd.read_csv(file_path) for file_path in csv_files}
    return df

def checkdata(dfs):
    cleaned_dfs = {}
    for key, value in dfs.items():
        df_copy = value.copy()
        
        df_copy = df_copy.drop_duplicates()
        df_copy = df_copy.fillna({"Calories": 130}) # Default calories value
        
        if 'Date' in df_copy.columns:
            df_copy['Date'] = pd.to_datetime(df_copy['Date'], format='mixed', errors='coerce')
            
        df_copy = df_copy.dropna() # N/A Check
        df_copy['Identifier'] = key # Storing filename stem as identifier
        
        cleaned_dfs[key] = df_copy
        
    return cleaned_dfs

def mergedata(df_dict):
    if not df_dict:
        return pd.DataFrame()
    mdf = list(df_dict.values())
    return pd.concat(mdf, ignore_index=True)


def menu(question, *options, type=1):
    print(f"\n{question}")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    while True:
        try:
            choice = int(input(f"Please choose an option from the list (1-{len(options)}): "))
            if choice in range(1, len(options) + 1):
                if type == 1:
                    return options[choice - 1]
                else:
                    return choice
        except ValueError:
            print(f"Please enter a valid number! (1-{len(options)})")


def view_stock_tickets():
    mdf = pd.read_csv("src/data/merged.csv")
    print("\nStock Identifiers: ")
    for ticket in mdf['Identifier'].unique():
        print(ticket)


def quit():
    print("Thank you for using the stock analysis program")
    exit()

def main():
    dfs = importCSV()
    if not dfs:
        return
        
    clean_dfs = checkdata(dfs)
    merge_dfs = mergedata(clean_dfs)
    
    if not merge_dfs.empty:
        merge_dfs.to_csv("src/data/merged.csv", index=False)
    
    while True:
        usr_choice = menu("Stock Analytics Menu","View available stocks","Explore and Visualise stock data","Exit",type=2)
        match usr_choice:
            case 1: view_stock_tickets()
            case 2: visualise()
            case 3: quit()
if __name__ == "__main__":
    main()