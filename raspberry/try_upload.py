import requests
# from pprint import pprint

url = 'http://127.0.0.1:8000/ecan/upload/'

data = {'ecan':'1', 'weight':'2.3'}
files = {'image_color': open('can.jpeg'),'image_ir':open('ir_can.jpg')}

r = requests.post(url, data = data, files=files)

response = requests.post('http://127.0.0.1:8000/ecan/upload/', files)
