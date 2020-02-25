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
       conexion = psycopg2.connect("dbname= user= password=")

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
       _full_name= request.form['name'] + request.form['surname']
       _email= request.form['email']
       _password= request.form['password']

       conexion = psycopg2.connect("host=animalicis.crl39vc3ngno.us-east-2.rds.amazonaws.com, database=Animalicis, user=postgres, password=Perros2012")
       cur = conexion.cursor()
       cur.execute( "SELECT email FROM users WHERE email_user= _email" )
       if cur.fetchall() is None:
          cur.execute( "INSERT INTO user (name_user, email_user, password_user) VALUES('_full_name', '_email', '_password')" )
          return "El usuario fue creado satisfactoriamente"
       else:
          return "El usuario ya esta registrado"
       conexion.close()

#def insert_user():
#    conexion = psycopg2.connect("dbname= user= password=")
#    cur = conexion.cursor()
#    cur.execute( "INSERT INTO user ('nickname','email','password') VALUES('')" )
#    cur.fetchall()

if __name__ == '__main__':
    app.run(debug=True)
