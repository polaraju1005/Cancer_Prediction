from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('cancerPrediction.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Predict',methods=['POST'])
def predict():
    Alcoholuse = (request.form.get('Alcoholuse'))
    DustAllergy = (request.form.get('DustAllergy'))
    OccuPationalHazards = (request.form.get('OccuPationalHazards'))
    GeneticRisk = (request.form.get('GeneticRisk'))
    chronicLungDisease = (request.form.get('chronicLungDisease'))
    BalancedDiet = (request.form.get('BalancedDiet'))
    Obesity = (request.form.get('Obesity'))
    PassiveSmoker = (request.form.get('PassiveSmoker'))
    ChestPain = (request.form.get('ChestPain'))
    CoughingofBlood = (request.form.get('CoughingofBlood'))
    Fatigue = (request.form.get('Fatigue'))
    ShortnessofBreath = (request.form.get('ShortnessofBreath'))
    FrequentCold = (request.form.get('FrequentCold'))

     # prediction
    result = model.predict(np.array([[Alcoholuse,DustAllergy,OccuPationalHazards,GeneticRisk,chronicLungDisease,BalancedDiet,Obesity,PassiveSmoker,ChestPain,CoughingofBlood,Fatigue,ShortnessofBreath,FrequentCold]]))
    if result[0] == 0:
        result = 'LOW'
    else:
        result = 'HIGH'

    return render_template('Predict.html',result=str(result))


if __name__ == '__main__':
    app.run(debug=True)