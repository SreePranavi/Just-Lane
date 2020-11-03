import numpy as np
import pygmaps
from flask import Flask, request, jsonify, render_template
import pickle
import geocoder
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime  
    
n=0
app = Flask(__name__)
model = pickle.load(open('model_knn.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('home.htm')
@app.route('/map.htm')
def map():
    return render_template('map.htm')
@app.route('/map1.htm')
def map1():
    return render_template('map1.htm')

@app.route('/predict',methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    mymap3 = pygmaps.maps(features[1], features[2], 15)    
    if prediction[0]==0:
        output="FCW - Imminent collisions Ahead!"
        mymap3.addpoint(features[1], features[2], "#FF0000") #red      
    elif prediction[0]==1:
        output="HB - Geographic Troubles in this area."
        mymap3.addpoint(features[1], features[2], "#925F4B")  #brown
    elif prediction[0]==2:
        output="HMW - A lot of traffic here!"
        mymap3.addpoint(features[1], features[2], "#0000FF") #blue
    elif prediction[0]==3:
        output="PCW - Watch Out!Pedestrians are Ahead"
        mymap3.addpoint(features[1], features[2], "#09F434") #green
    elif prediction[0]==4:
        output="Stoppage - Looks like you're gonna stop."
        mymap3.addpoint(features[1], features[2], "#925F4B")
    mymap3.addradpoint(features[1], features[2],150, "#000000")
    points1(features,mymap3,n)
    points2(features,mymap3,n)
    points3(features,mymap3,n)
    points4(features,mymap3,n)
    mymap3.draw(r'C:\Users\Sarvesh\Desktop\Intel\templates\map.htm')
    return render_template('result.htm', prediction_text='Predicted Value: {}'.format(output))


def points1(features,mymap3,n):
    if n==2:
        return
    la=features[1]
    lo=features[2]
    la=la+0.008983 
    lo=lo+0.015060
    temp=[features[0],la,lo]
    fin_temp=[temp]
    pred = model.predict(fin_temp)
    if pred[0]==0:
        mymap3.addpoint(temp[1], temp[2], "#FF0000") #red      
    elif pred[0]==1:
        mymap3.addpoint(temp[1], temp[2], "#925F4B")  #brown
    elif pred[0]==2:
        mymap3.addpoint(temp[1], temp[2], "#0000FF") #blue
    elif pred[0]==3:
        mymap3.addpoint(temp[1], temp[2], "#09F434") #green
    elif pred[0]==4:
        mymap3.addpoint(temp[1], temp[2], "#925F4B")
    n=n+1
    points1(temp,mymap3,n)
def points2(features,mymap3,n):
    if n==2:
        return
    la=features[1]
    lo=features[2]
    la=la-0.008983 
    lo=lo-0.015060
    temp=[features[0],la,lo]
    fin_temp=[temp]
    pred = model.predict(fin_temp)
    if pred[0]==0:
        mymap3.addpoint(temp[1], temp[2], "#FF0000") #red      
    elif pred[0]==1:
        mymap3.addpoint(temp[1], temp[2], "#925F4B")  #brown
    elif pred[0]==2:
        mymap3.addpoint(temp[1], temp[2], "#0000FF") #blue
    elif pred[0]==3:
        mymap3.addpoint(temp[1], temp[2], "#09F434") #green
    elif pred[0]==4:
        mymap3.addpoint(temp[1], temp[2], "#925F4B")
    n=n+1
    points2(temp,mymap3,n)
def points3(features,mymap3,n):
    if n==2:
        return
    la=features[1]
    lo=features[2]
    la=la-0.008983 
    lo=lo+0.015060
    temp=[features[0],la,lo]
    fin_temp=[temp]
    pred = model.predict(fin_temp)
    if pred[0]==0:
        mymap3.addpoint(temp[1], temp[2], "#FF0000") #red      
    elif pred[0]==1:
        mymap3.addpoint(temp[1], temp[2], "#925F4B")  #brown
    elif pred[0]==2:
        mymap3.addpoint(temp[1], temp[2], "#0000FF") #blue
    elif pred[0]==3:
        mymap3.addpoint(temp[1], temp[2], "#09F434") #green
    elif pred[0]==4:
        mymap3.addpoint(temp[1], temp[2], "#925F4B")
    n=n+1
    points3(temp,mymap3,n)
def points4(features,mymap3,n):
    if n==2:
        return
    la=features[1]
    lo=features[2]
    la=la+0.008983 
    lo=lo-0.015060
    temp=[features[0],la,lo]
    fin_temp=[temp]
    pred = model.predict(fin_temp)
    if pred[0]==0:
        mymap3.addpoint(temp[1], temp[2], "#FF0000") #red      
    elif pred[0]==1:
        mymap3.addpoint(temp[1], temp[2], "#925F4B")  #brown
    elif pred[0]==2:
        mymap3.addpoint(temp[1], temp[2], "#0000FF") #blue
    elif pred[0]==3:
        mymap3.addpoint(temp[1], temp[2], "#09F434") #green
    elif pred[0]==4:
        mymap3.addpoint(temp[1], temp[2], "#925F4B")
    n=n+1
    points4(temp,mymap3,n)
    
@app.route('/curr',methods=['POST'])
def curr():
    features = [float(x) for x in request.form.values()]
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(executable_path = './chromedriver.exe', options=options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(1)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = float(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = float(latitude[0])
    driver.quit()
    features.append(latitude)
    features.append(longitude)
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    mymap3 = pygmaps.maps(features[1], features[2], 15)
    if prediction[0]==0:
        output="FCW - Imminent collisions Ahead!"
        mymap3.addpoint(features[1], features[2], "#FF0000") #red      
    elif prediction[0]==1:
        output="HB - Geographic Troubles in this area."
        mymap3.addpoint(features[1], features[2], "#925F4B")  #brown
    elif prediction[0]==2:
        output="HMW - A lot of traffic here!"
        mymap3.addpoint(features[1], features[2], "#0000FF") #blue
    elif prediction[0]==3:
        output="PCW - Watch Out!Pedestrians are Ahead"
        mymap3.addpoint(features[1], features[2], "#09F434") #green
    elif prediction[0]==4:
        output="Stoppage - Looks like you're gonna stop."
        mymap3.addpoint(features[1], features[2], "#925F4B") #brown
    points1(features,mymap3,n)
    points2(features,mymap3,n)
    points3(features,mymap3,n)
    points4(features,mymap3,n)
    mymap3.addradpoint(features[1], features[2],150, "#000000")
    mymap3.draw(r'C:\Users\Sarvesh\Desktop\Intel\templates\map1.htm')
    return render_template('result.htm', prediction_text='Predicted Value: {}'.format(output))
@app.route('/currtime',methods=['POST'])
def currtime():
    current_time = datetime.datetime.now() 
    features = [float(current_time.hour)]
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(executable_path = './chromedriver.exe', options=options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(1)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = float(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = float(latitude[0])
    driver.quit()
    features.append(latitude)
    features.append(longitude)
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    mymap3 = pygmaps.maps(features[1], features[2], 15)
    if prediction[0]==0:
        output="FCW - Imminent collisions Ahead!"
        mymap3.addpoint(features[1], features[2], "#FF0000") #red      
    elif prediction[0]==1:
        output="HB - Accident Prone Zone"
        mymap3.addpoint(features[1], features[2], "#925F4B")  #brown
    elif prediction[0]==2:
        output="HMW - A lot of traffic here!"
        mymap3.addpoint(features[1], features[2], "#0000FF") #blue
    elif prediction[0]==3:
        output="PCW - Watch Out!Pedestrians are Ahead"
        mymap3.addpoint(features[1], features[2], "#09F434") #green
    elif prediction[0]==4:
        output="Stoppage - Accident Prone Zone"
        mymap3.addpoint(features[1], features[2], "#925F4B") #brown
    points1(features,mymap3,n)
    points2(features,mymap3,n)
    points3(features,mymap3,n)
    points4(features,mymap3,n)
    mymap3.addradpoint(features[1], features[2],150, "#000000")
    mymap3.draw(r'C:\Users\Sarvesh\Desktop\Intel\templates\map1.htm')
    return render_template('result.htm', prediction_text='Predicted Value: {}'.format(output))
@app.route('/results',methods=['POST'])
def results():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
