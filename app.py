from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('abc.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        shop_id = int(request.form['shop_id'])
        item_id=float(request.form['item_id'])
        item_price=int(request.form['item_price'])
        prediction=model.predict([[34,shop_id,item_id,item_price,0,0,0,0,0,0]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry no items sold")
        else:
            return render_template('index.html',prediction_text="Number of items sold per month are {}".format(output))
    else:
        return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)

