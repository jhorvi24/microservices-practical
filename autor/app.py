#servicio web para mostrar información sobre autores de libros

from flask import Flask, render_template, jsonify, redirect
import json
import socket

app = Flask(__name__)

def get_ip():    
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip


@app.route('/authors')
def index():
    hostname, ip = get_ip()    
    
    return render_template('index.html',HOSTNAME=hostname, IP=ip)

@app.route('/authors/list')
def autores():
    json_file = open('autores.json')
    data = json.load(json_file)   
    return jsonify(data), 200

#Leer el id del archivo json
@app.route('/authors/list/<int:id>', methods=['GET'])
def reviewID(id):
    with open('autores.json') as json_file:
        data = json.load(json_file)        
    rev=data['authors']  
    for i in rev:        
        if i["id"]==id:
            return jsonify(i)        
    return jsonify("No se encotró el autor")

        
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
    return jsonify('OK'),200

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)