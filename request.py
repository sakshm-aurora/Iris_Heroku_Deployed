import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'petal_length':5.2, 'petal_width':3.5, 'sepal_length':2.4 , 'sepal_width':1.2 })

print(r.json())
