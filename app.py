from flask import Flask , jsonify , make_response,request,render_template
from flask_cors import CORS
import pickle
import numpy as np
import os

def predictions(req):
  data = request.get_json(force = True)
  param1 = data["sepalLength"]
  param2 = data['sepalWidth']
  param3 = data['petalLength']
  param4 = data['petalWidth']
  pred = np.array([[param1 , param2 ,param3 ,param4]], dtype = np.float)
  y_pred = imp_model.predict(pred)
  print(y_pred[0])
  return(y_pred[0])

imp_model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)
CORS(app)
@app.route('/',methods = ["GET","POST"])
def index():
  if request.method == 'POST':
    return jsonify(results = int(predictions(request)))
  else :
    return ("server is running...")
@app.route('/predict', methods = ['GET','POST'])
def predict():
  if request.method == 'POST':
    return jsonify(results = int(predictions(request)))
  else :
    return ("server is running..")
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = int(os.environ.get("PORT",8080)))
