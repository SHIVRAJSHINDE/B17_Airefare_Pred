from flask import Flask, request, render_template
from src.S2_prediction.S1_Prediction import PredictionClass

app = Flask(__name__)

app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method==["GET"]:
        return render_template("home.html")

    PredictionObj = PredictionClass()
    df = PredictionObj.receiveDataFromWeb()
    print(df)

    return render_template("home.html",prediction_text=f"Your Flight price is Rs. {df}",)


if __name__== "__main__":
    app.run(host="0.0.0.0",debug=True)