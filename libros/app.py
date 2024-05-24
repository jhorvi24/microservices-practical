#aplicación utilizando microservicios y flask para solicitar una lista de libros disponibles

from flask import Flask, render_template, request, jsonify, redirect
import os
import json
import socket
app = Flask(__name__)

AUTOR_SERVICE_URL = os.getenv('AUTOR_SERVICE_URL')
LIBRO_SERVICE_URL = os.getenv('LIBRO_SERVICE_URL')
CALIFICACION_SERVICE_URL = os.getenv('CALIFICACION_SERVICE_URL')

def get_ip():    
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip

@app.route('/books')
def index():
    hostname, ip = get_ip()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)
     
     
@app.route('/books/catalog', methods=['GET'])
def libros():
    #Read the json file
    json_file = open('libros.json')
    data = json.load(json_file)       
    return jsonify(data), 200

#Leer el id del archivo json
@app.route('/books/catalog/<int:id>', methods=['GET'])
def reviewID(id):
    with open('libros.json') as json_file:
        data = json.load(json_file)        
    rev=data['libros']  
    for i in rev:        
        if i["book-id"]==id:
            return jsonify(i)        
    return jsonify("No se encotró el libro")  

@app.route('/autor')
def autor():
    url = AUTOR_SERVICE_URL 
    return redirect(url)
    
    
@app.route('/calificacion')
def calificacion():
    url = CALIFICACION_SERVICE_URL  
    return redirect(url)

@app.route('/health')
def health():
    return jsonify("OK"),200


   

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5002)
    

