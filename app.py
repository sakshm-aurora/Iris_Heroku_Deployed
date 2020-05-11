import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 3)
    def output_string(output):
    	if output == 0 :
    		return 'Setosa'
    	elif output == 1:
    		return 'Versicolor'
    	else :
    		return 'Virginica'

    result = output_string(output)

    return render_template('index.html', prediction_text='The predicted iris flower is {}'.format(result))


if __name__ == "__main__":
    app.run(debug=True)