from flask import Flask, request, render_template
import joblib
import pandas as pd


class PredictionClass:
    def __init__(self):
        self.airline = request.form.get("Airline")
        self.date_of_journey = request.form.get("Dep_Time")
        self.source = request.form.get("Source")
        self.destination = request.form.get("Destination")
        self.arrival_time = request.form.get("Arrival_Time")
        self.total_stops = request.form.get("Total_Stops")

    def receiveDataFromWeb(self):
        dictOne = {
            "Airline": [self.airline],
            "Date_of_Journey": [self.date_of_journey],
            "Source": [self.source],
            "Destination": [self.destination],
            "Arrival_Time": [self.arrival_time],
            "DurHrs_Mins": [0],
            "Total_Stops": [self.total_stops]
        }

        df = pd.DataFrame(dictOne)
        return df

    def convertArr_n_DeptTime_Duration(self,df):
        print("_______________Duration_____________")

        print(df)
        df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'],format='mixed')
        df['Arrival_Time'] = pd.to_datetime(df['Arrival_Time'],format='mixed')

        total_Duration = df['Arrival_Time'] - df['Date_of_Journey']
        print(total_Duration)
        total_Duration = total_Duration.dt.total_seconds() / 60

        df['DurHrs_Mins'] = total_Duration.astype(int)
        print("------Duration-S-Completed")
        return df

    def drop_Col_From_web(self,df):
        df = df.drop(['Date_of_Journey','Arrival_Time'],axis=1)
        return df