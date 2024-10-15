from flask import Flask,render_template,request
import pandas as pd
from src.utils import load_object
from src.utils import config
import os,sys
from src.logger import logging
from src.exception import CustomException

model_path=os.path.join(config.model_trainer.model_path,'model.pkl')
preprocessor_pth=os.path.join(config.data_transform.preprocessor_path,'preprocessor.pkl')

model=load_object(model_path)
preprocssor=load_object(preprocessor_pth)


app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def predict():
    try:
        logging.info("Data is loading into variables from form ")
        data = {
            'Age': int(request.form['age']),
            'Sex': request.form['sex'],
            'Job': int(request.form['job']),
            'Housing': request.form['housing'],
            'Saving accounts': request.form['saving_accounts'],
            'Checking account': request.form['checking_account'],
            'Credit amount': int(request.form['credit_amount']),
            'Duration': int(request.form['duration']),
            'Purpose': request.form['purpose']
        }
        df_pred=pd.DataFrame([data])
        logging.info("Data is loaded in a dataframe ")
        print(df_pred)
        df_scaled=preprocssor.transform(df_pred)
        y_pred=model.predict(df_scaled)
        return render_template('home.html',results=y_pred[0])
    except Exception as e:
        raise CustomException(e,sys)

if __name__=='__main__':
    app.run(debug=True)