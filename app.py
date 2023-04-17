from tamagotchi import Tamagotchi
from flask import Flask, render_template, jsonify

app = Flask(__name__)

tama = Tamagotchi("patito jose")
#print(tama)
#print(tama.nombre)
#print(tama.seriallize())
#print(tama.crecer())
#print(tama.crecer())
#print(tama.crecer())
#print(tama.crecer())

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', tama = tama.seriallize())

@app.route('/crecer', methods=['GET'])
def comer():

    mensaje = tama.crecer()

    return jsonify({
        "mensaje": mensaje
    })

@app.route('/status', methods=['GET'])
def show_status():
    return jsonify(tama.seriallize())
        
#definiendo que este archivo es el principal de la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)