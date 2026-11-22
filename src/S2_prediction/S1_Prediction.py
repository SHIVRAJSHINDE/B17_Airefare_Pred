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