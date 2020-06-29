from flask import Flask , jsonify , make_response,request
import pickle
import numpy as np
import os
imp_model = pickle.load(open('/content/model.pk1','rb'))
app = Flask(__name__)
@app.route('/',methods = ["GET"])
def index():
  return "server is running..."
@app.route('/predict', methods = ['POST'])
def predict():
  data = request.get_json(force = True)
  param1 = int(data["sepallength"])
  param2 = int(data["sepalwidth"])
  param3 = int(data["petallength"])
  param4 = int(data["petalwidth"])
  pred = np.array([[param1 , param2 ,param3 ,param4]], dtype = np.float)
  y_pred = imp_model.predict(pred)
  print(y_pred[0])
  return jsonify(results = int(y_pred[0]))

if __name__ == '__main__':
 app.run(port= int(os.environ.get("PORT") or 8080 ))
