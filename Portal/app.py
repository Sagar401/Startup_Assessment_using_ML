import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# transform_model = pickle.load(open('scaler_transform.pkl', 'rb'))
#modelApp = pickle.load(open('logreg_App.pkl', 'rb'))
modelApp = pickle.load(open('RFclassifier.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')    

@app.route('/Analysis')
def Analysis():
    return render_template("Analysis.html")

@app.route('/Team')
def Team():
    return render_template("Team.html")

@app.route('/EDA')
def EDA():
    return render_template("EDA.html")

@app.route('/EDAStartupWithSocial')
def EDAStartupWithSocial():
    return render_template("EDAforStartupWithSocial.html")

@app.route('/PredictionWithSocial')
def PredictionWithSocial():
    return render_template("ModelPerformanceWithSocialData.html")

@app.route('/DT')
def DT():
    return render_template("DT.html")

@app.route('/ComparativeStudy')
def ComparativeStudy():
    return render_template("ComparativeStudy.html")

    

@app.route('/SurvivalAnalysisForApp')
def SurvivalAnalysisForApp():
    return render_template("SurvivalAnalysisForApp.html")

@app.route('/MainDashboard')
def MainDashboard():
    return render_template("MainDashboard.html")

@app.route('/SeedDT')
def SeedDT():
    return render_template("SeedDT.html")

@app.route('/SeriesDT')
def SeriesDT():
    return render_template("SeriesDT.html")

@app.route('/DTOperating')
def DTOperating():
    return render_template("DTOperating.html")

@app.route('/OperCloseForApp')
def OperCloseForApp():
    return render_template("StartupOperCloseAnalysisForApp.html")

# def estimator(to_predict_list):
#     test = to_predict_list
#     print(test)
#     # reshapping the input in the shape according to the featur columns
#     to_predict = np.array(to_predict_list).reshape(1, 9)
#     # importing the model and standard scaler from the pickel file
#     std_scl = pickle.load(open("scaler_transform.pkl", "rb"))
#     final_ar = std_scl.transform(to_predict)
#     loaded_model = pickle.load(open("logistic_reg.pkl", "rb"))
#     result = loaded_model.predict_proba(final_ar)
#     # print(loaded_model.predict_proba(final_ar))
#     print(result)
#     return result


# @app.route('/result', methods=['POST'])
# def result():
#     if request.method == 'POST':
#         to_predict_list = request.form.to_dict()
#         to_predict_list = list(to_predict_list.values())
#         to_predict_list = list(map(int, to_predict_list))
#         result = estimator(to_predict_list)
#         print(result)
#         success = result[0][1]
#         print(success)
#         return render_template("result.html", prediction=success)



@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=modelApp.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)
    return render_template('index.html',pred='The chances of startup to be in Operational stage is {}'.format(output))

    # if output>str(0.5):
    #     return render_template('index.html',pred='Startup will be operating.\nProbability of Successful operation occuring is {}'.format(output))
    # else:
    #     return render_template('index.html',pred='Startup may not be operating.\n Probability of CLOSED operation is {}'.format(output))




if __name__ == "__main__":
    app.run(debug=True)