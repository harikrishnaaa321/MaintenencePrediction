from django.shortcuts import render
#from joblib import load
import joblib
from sklearn.preprocessing import LabelEncoder
model = joblib.load('./savedModels/model.joblib')
label_encoder = LabelEncoder()
def predictor(request):
 if request.method=='POST':
    Type = request.POST['Type']
    AirTemperature = request.POST['AirTemperature']
    ProcessTemperature =  request.POST['ProcessTemperature']
    Torque = request.POST['Torque']
    ToolWear = request.POST['ToolWear']
    Rotationalspeed = request.POST['Rotationalspeed']
    temperatureDifference = request.POST['temperatureDifference']
    Type_encoded = label_encoder.fit_transform(['Type'])[0]

    y_pred = model.predict([[Type_encoded,AirTemperature,
                             ProcessTemperature,Rotationalspeed,Torque,ToolWear,temperatureDifference,1]])
    if y_pred[0] == 0:
        y_pred = " No Failure"
    elif y_pred[0] == 1:
        y_pred = "Power Failure"
    elif y_pred[0] == 2:
        y_pred = "tool wear"
    elif y_pred[0] == 3:
        y_pred = "overstrain failure"
    elif y_pred[0] == 4:
        y_pred = "RAndom FAilure"
    elif y_pred[0] == 5:
        y_pred = "Heat Dissipation"
    return render(request,'main.html',{'result':y_pred})
 return render(request,'main.html')
