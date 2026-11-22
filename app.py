from flask import Flask, request, render_template
from src.S2_prediction.S1_Prediction import PredictionClass
from src.train_ppln.s1_DataCleaning import Data_Cleaning

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method==["GET"]:
        return render_template("home.html")

    PredictionObj = PredictionClass()
    df = PredictionObj.receiveDataFromWeb()
    df = PredictionObj.convertArr_n_DeptTime_Duration(df)

    cleaningObj = Data_Cleaning
    df = cleaningObj.DateTimeConverion(df)
    df = PredictionObj.drop_Col_From_web(df)
    df = PredictionObj.transform_web_Data(df)
    output = PredictionObj.final_prediction(df)

    # print(df)
    # print(df.T)

    return render_template("home.html",prediction_text=f"Your Flight price is Rs. {output}",)


if __name__== "__main__":
    app.run(host="0.0.0.0",debug=True)