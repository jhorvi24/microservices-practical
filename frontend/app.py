
from flask import Flask, render_template, request, jsonify, redirect
import json
import socket
import requests
import os

app = Flask(__name__)

AUTOR_SERVICE_URL = os.getenv('AUTOR_SERVICE_URL')
LIBRO_SERVICE_URL = os.getenv('LIBRO_SERVICE_URL')
CALIFICACION_SERVICE_URL = os.getenv('CALIFICACION_SERVICE_URL')

def get_ip():    
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip

@app.route('/')
def index():
    hostname, ip = get_ip()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)  

@app.route('/autor')
def autor():
    url ='http://localhost:5000'   
    return redirect(url)
    
    
@app.route('/calificacion')
def calificacion():
    url ='http://localhost:5001'   
    return redirect(url)

@app.route('/libros')
def libros():
    url ='http://localhost:5002'   
    return redirect(url)   

@app.route('/health')
def health():
    return jsonify("OK"),200

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5003)