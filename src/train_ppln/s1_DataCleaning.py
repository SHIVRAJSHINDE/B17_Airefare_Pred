class Data_Cleaning:
    def readFile():
     df = pd.read_csv("E:/1.Eathans/Ethans/Data/Airline/Airline1.csv")
     return df

    def Handel_Missing(df):
        missin_COL = ['Source','Destination','Route','Total_Stops']
        for i in missin_COL:
            Missing = df[i].mode()[0]
            df.fillna({i:Missing},inplace=True)
            
        Missing_Price = df['Price'].mean()
        df.fillna({'Price':Missing_Price},inplace=True)
        return df

    def Handle_Duplicates(df):
        df.drop_duplicates(inplace=True)
        df[df.duplicated()]
        return df

    def Replace_Uneve(df):
        df['Destination'] = df['Destination'].replace({"New Delhi":"Delhi"})
        return df

    def convertDur_Min(df):
        for i in df.index:
            ColOne = df.loc[i,'Duration'].split()[0]
            ColTwo = df.loc[i,'Duration'].split()[1]
            
            if "h" in ColOne:
                ColOne = int(ColOne.replace("h",""))*60
            elif "m" in ColOne:
                ColOne = int(ColOne.replace("m",""))

            if "h" in ColTwo:
                ColTwo = int(ColTwo.replace("h",""))*60
            elif "m" in ColTwo:
                ColTwo = int(ColTwo.replace("m",""))
            
            df.loc[i,'DurHrs_Mins'] = ColOne + ColTwo
        return df

    def DateTimeConverion(df):
        df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'],format='mixed')
        df['D_day'] = df['Date_of_Journey'].dt.day
        df['D_month'] = df['Date_of_Journey'].dt.month
        df['D_year'] = df['Date_of_Journey'].dt.year
        df['D_hours'] = df['Date_of_Journey'].dt.hour
        df['D_minutes'] = df['Date_of_Journey'].dt.minute

        df['Arrival_Time'] = pd.to_datetime(df['Arrival_Time'],format='mixed')
        df['A_day'] = df['Arrival_Time'].dt.day
        df['A_month'] = df['Arrival_Time'].dt.month
        df['A_year'] = df['Arrival_Time'].dt.year
        df['A_hours'] = df['Arrival_Time'].dt.hour
        df['A_minutes'] = df['Arrival_Time'].dt.minute
        return df

    def uncessaryCol(df):
        col_Drop = ['ID','Date_of_Journey','Route','Dep_Time',
                    'Arrival_Time','Duration','Additional_Info']
        df.drop(col_Drop,axis=1,inplace=True)
        return df


    def saveCleanedData(df):
        file_Path = "Airtifacts/Clnd_Data/Cleaned_Data.csv"
        df.to_csv(file_Path,index=False)