from src.train_ppln.s1_DataCleaning import Data_Cleaning
from src.train_ppln.s2_Tranform import Transform
from src.train_ppln.s3_Act_Training import Trainning
import joblib

if __name__ == "__main__":
    obj_Cleaning  = Data_Cleaning
    df = obj_Cleaning.readFile()
    df = obj_Cleaning.Handel_Missing(df)
    df = obj_Cleaning.Handle_Duplicates(df)
    df = obj_Cleaning.Replace_Uneve(df)
    df = obj_Cleaning.convertDur_Min(df)
    df = obj_Cleaning.DateTimeConverion(df)
    df = obj_Cleaning.uncessaryCol(df)
    df = obj_Cleaning.remove_Outlier(df)
    obj_Cleaning.saveCleanedData(df)

    Obj_Trans = Transform()
    df = Obj_Trans.readData()
    X_train,X_test,y_train_true,y_test_true = Obj_Trans.Train_Test_Split(df)
    trans_Obj = Obj_Trans.transform_Data()
    X_train_trans = trans_Obj.fit_transform(X_train)
    X_train_trans.to_csv("Airtifacts/Trans_Data/X_train_trans.csv",index=False)
    joblib.dump(trans_Obj,"Airtifacts/pkl_TransFile/trans_Obj.pkl")
    X_test_trans = trans_Obj.transform(X_test)
    X_test_trans.to_csv("Airtifacts/Trans_Data/X_test_trans.csv",index=False)

    Obj_Train = Trainning()
    X_test, X_train, X_train_trans, X_test_trans, y_train_true, y_test_true = Obj_Train.readData()
    Obj_Train.Model_Training(X_train_trans,X_test_trans,X_train,X_test,y_train_true, y_test_true)
    
