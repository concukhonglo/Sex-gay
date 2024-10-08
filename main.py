from flask import Flask, request
import time

app = Flask(__name__)

data_base_phake = {}

@app.route('/')
def home():
    return 'Home'

@app.route('/checkkey')
def checkkey():
    key = request.args.get('key')
    data =  {'success': key in data_base_phake and round(time.time()) < data_base_phake[key]}
    if data['success']:
        data['remain_time'] = data_base_phake[key]
    return data

@app.route('/addkey')
def addkey():
    key = request.args.get('key')
    data_base_phake[key] = round(time.time()) + 30 * 24 * 60 * 60
    return 'Đã thêm key'

@app.route('/deletekey')
def delete_key():
    key = request.args.get('key')
    del data_base_phake[key]
    return 'OK'




app.run('0.0.0.0', port=8000)




