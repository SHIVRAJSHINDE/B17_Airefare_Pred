from src.train_ppln.s1_DataCleaning import Data_Cleaning

if __name__ == "__main__":
    obj_Cleaning  = Data_Cleaning
    df = obj_Cleaning.readFile()
    print(df.head(2))