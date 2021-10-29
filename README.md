# domains-quality-checker
an API to check if a url or IP address  is safe or phishing.
Using a ML model.

## Install the requirements
pip install -r requirements.txt

## Run the server
cd path/to/project/folder
uvicorn api:app

## Request url format
http://127.0.0.1:8000/predict?input='url or ip_adress'

## API responses :
- if the data saved seccessfully. 
responce = {
    'input':'url or ip_adress',
    'Prediction':'safe'or 'phishing',
    'Status' :'Data saved seccessfully'
}
- if the url or ip_adress not entred in a correct format. 
responce = {
    'input':'url or ip_adress',
    'Status': 'Invalid input format'
}

- Sometimes the number of features generated of url not equal to 30, if it is the case : 
responce = {
    'input':'url or ip_adress',
    'Status': 'Number of features generated not equal to 30'
}

## demo
py demo.py

## saved data directory
project_path/db
