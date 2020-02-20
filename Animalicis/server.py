# 1)Autenticación de formularios (Signup, login)
# 2)conectar liks de barra de tareas
# 3)Autenticación filtro de sección de adopcion
# 4)Visualización de animales disponibles para adopción
# 5)Conectar formularios a base de datos
# 6)Mapa de refugios
# 7)Listados de eventos

import psycopg2

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/login', methods=['GET'])
def login():
    return app.send_static_file('login.html')

@app.route('/signup', methods=['GET'])
def signup():
    return app.send_static_file('signup.html')

@app.route('/processLogin', methods=['GET', 'POST'])
def processLogin():
       missing = []
       fields = ['email', 'passwd', 'login_submit']
       for field in fields:
              value = request.form.get(field, None)
              if value is None:
                  missing.append(field)
       if missing:
              return "Warning: Some fields are missing"

@app.route('/processSignup', methods=['GET', 'POST'])
def processSignup():
       missing = []
       fields = ['nickname', 'email', 'passwd','confirm', 'signup_submit']
       for field in fields:
              value = request.form.get(field, None)
              if value is None:
                     missing.append(field)
       if missing:
              return "Warning: Some fields are missing"

if __name__ == '__main__':
    app.run(debug=True)
