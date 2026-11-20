import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor,GradientBoostingRegressor



class Trainning:
    def __init__(self):
        self.models = {"GraBoostRegressor":GradientBoostingRegressor()}
        self.params = {"GraBoostRegressor":{}}

    def readData(self):
        X_test = pd.read_csv("Airtifacts\Clnd_Data\X_test.csv")
        X_train = pd.read_csv("Airtifacts\Clnd_Data\X_train.csv")

        X_train_trans = pd.read_csv("Airtifacts\Trans_Data\X_train_trans.csv")
        X_test_trans = pd.read_csv("Airtifacts\Trans_Data\X_test_trans.csv")
        y_train_true = pd.read_csv("Airtifacts\Clnd_Data\y_train_true.csv")
        y_test_true = pd.read_csv("Airtifacts\Clnd_Data\y_test_true.csv")

        return X_test, X_train, X_train_trans, X_test_trans, y_train_true, y_test_true

    def linear_Metrics(self,X_Data,y_true,y_pred):
        MSE = mean_squared_error(y_true,y_pred) 
        MAE = mean_absolute_error(y_true,y_pred)
        RMSE = root_mean_squared_error(y_true,y_pred)
        R2 = r2_score(y_true,y_pred)

        n = len(X_Data)
        p = X_Data.shape[1]
        A_R2 = 1-(1-R2)*(n-1)/(n-p-1)
        measures ={"MSE":[MSE],
                    "MAE":[MAE],
                    "RMSE":[RMSE],
                    "R2":[R2],
                    "A_R2":[A_R2]} 
        measures = pd.DataFrame(measures)
        print(measures)

    def Model_Training(self,X_train_trans,X_test_trans,X_train,X_test,y_train_true, y_test_true):

        y_train_true = y_train_true.to_numpy().ravel()
        y_test_true = y_test_true.to_numpy().ravel()

        for model_Name, act_Model in self.models.items():
            grid_obj = GridSearchCV(act_Model,self.params[model_Name])
            grid_obj.fit(X_train_trans,y_train_true)    # Training phase
            best_model_with_par = grid_obj.best_estimator_
            joblib.dump(best_model_with_par,f"Airtifacts/pklModels/{model_Name}.pkl")
            y_train_pred = best_model_with_par.predict(X_train_trans)
            print(model_Name)
            print("Train")
            self.linear_Metrics(X_train,y_train_true,y_train_pred)
            
            print("Test")
            y_test_pred = best_model_with_par.predict(X_test_trans)

            self.linear_Metrics(X_test,y_test_true,y_test_pred)
