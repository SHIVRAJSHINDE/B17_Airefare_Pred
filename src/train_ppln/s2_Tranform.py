
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder,StandardScaler
import joblib


class Transform:
    def readData(self):
        df = pd.read_csv("Airtifacts\Clnd_Data\Cleaned_Data.csv")
        return df

    def Train_Test_Split(self,df):
        y = df['Price']
        X = df.drop('Price',axis=1)
        X_train,X_test,y_train_true,y_test_true =train_test_split(
                                X,y,test_size=.20,random_state=42)

        X_train.to_csv("Airtifacts/Clnd_Data/X_train.csv",index=False)
        X_test.to_csv("Airtifacts/Clnd_Data/X_test.csv",index=False)

        y_train_true.to_csv("Airtifacts/Clnd_Data/y_train_true.csv",index=False)
        y_test_true.to_csv("Airtifacts/Clnd_Data/y_test_true.csv",index=False)
        
        return X_train,X_test,y_train_true,y_test_true

    def transform_Data(self):
        One_Hot_Columns = ["Airline","Source","Destination"]
        Ordered_Columns = ["Total_Stops"]
        Total_Stops_Order = ['non-stop', '1 stop','2 stops', '3 stops', '4 stops']
        Numerical_Colums = ["DurHrs_Mins","D_day","D_month","D_year","D_hours","D_minutes","A_day","A_month","A_year","A_hours","A_minutes"]

        OneHot_E =  ("O_H_E",OneHotEncoder(sparse_output=False,drop='first',handle_unknown="ignore"),One_Hot_Columns,)

        Ordinal_E = ("O_E",OrdinalEncoder(categories=[Total_Stops_Order]),Ordered_Columns,)
        Scaling = ("N_C", StandardScaler(), Numerical_Colums)

        trans_Obj = ColumnTransformer(transformers=[Ordinal_E,OneHot_E,Scaling]).set_output(transform="pandas")

        return trans_Obj
