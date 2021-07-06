import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#app = Flask(__name__)
app = Flask(__name__, template_folder='templates')

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
#@app is flask imported object app
def home():
    return render_template('index.html')


# This is the post method, wherein input some features to model.pkl file to predict the op
# Here /predict is calling below function predict
@app.route('/predict',methods=['POST'])
#@app is flask imported object app
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #Here  request.form.values() will read all the features
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

# Comment this while deploying in cloud and uncomment below another script
#if __name__ == "__main__":
#    app.run(debug=True)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
	#@app is flask imported object app