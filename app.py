import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('Finalized_Model.pickle', 'rb'))
scaler = StandardScaler()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(item) for item in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(scaler.fit_transform(final_features))

    print(prediction)
    return render_template('index.html', prediction_text='Admission Percentage  {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)