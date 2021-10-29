import requests

inputs = ['https://www.google.com/','https://www.stackoverflow.com/','https://www.geeksforgeeks.org/',
            'https://www.freelancer.com/','10.255.255.255','192.168.255.0','http://172.31.0.0']

for input in inputs :
    resp = requests.get(f'http://127.0.0.1:8000/predict?input={input}')
    print(resp.json())