# 1)Autenticación de formularios (Signup, login) (pendiente de probar)
# 2)conectar liks de barra de tareas (en proceso)
# 3)Autenticación filtro de sección de adopcion (en proceso)
# 4)Visualización de animales disponibles para adopción (en proceso)
# 5)Conectar formularios a base de datos (en simultaneo)
# 6)Mapa de refugios (pospuesto)
# 7)Listados de eventos (pendiente)

import json
import psycopg2

#from PIL import Image, ImageOps
from flask import Flask, request, url_for, redirect
app = Flask(__name__)



@app.route('/', methods=['GET']) #probar con colocar la paguina donde esta subido el index
def index():#poner variable base para la seleccion de raza MAXIMA URJENCIA TERMINAR!!!!!
    return app.send_static_file('index.html')

@app.route('/account', methods=['GET'])                                         #enlace a la eleccion de perfil
def account():
    return app.send_static_file('cuentas.html')

@app.route('/profile', methods=['GET'])#pendiente de crear                      #perfil visible solo por el usuario
def profile():#terminar
    return app.send_static_file('perfil.html')

@app.route('/profileV', methods=['GET'])#pendiente de crear                     #perfil visible por el resto de usuario
def profileV():#terminar
    return app.send_static_file('perfil.html')

@app.route('/signup', methods=['GET'])
def signup():
    return app.send_static_file('signup.html')

@app.route('/signUpdate', methods=['GET'])                                      #(((Enlace al formulario de Up Date del usuario)))
def signUpdate():#escribir nombre del html una ves este
    return app.send_static_file('formulsrio de up date.html')

@app.route('/signupRef', methods=['GET'])
def signupRef():
    return app.send_static_file('SignupRef.html')

@app.route('/signupRefUpdate', methods=['GET'])                                 #(((Enlace al formulario de Up Date del refugio)))
def signupRefUpdate():#escribir nombre del html una ves este
    return app.send_static_file('formulsrio de up date.html')

@app.route('/processLogin', methods=['GET', 'POST'])
def processLogin():# (usar las funciones de search_data y insert_data)
        _email= "'" + str(request.args.get('email', None)) + "'"
        _password= "'" +  str(request.args.get('contraseña', None)) + "'"

        sql_search_user= "SELECT email_user, password_user FROM users WHERE email_user ={} AND password_user ={}".format(_email, _password)
        sql_search_ref= "SELECT email_refuge, password_refuge FROM refuges WHERE email_refuge ={} AND password_refuge ={}".format(_email, _password)
        sql="SELECT * FROM users"

        row= search_data(sql_search_ref)
        if row is None:
            row= search_data(sql_search_user)
            if row is None:
                return  "Correo y/o contraceña incorrecta"
            else:
                usuario= redirect(url_for('index'))#para crear una cookie y guardar los datos del Usuario
                usuario.set_cookie("User", json.dumps(dict(request.form.items())))#en el navegador
                return usuario
        else:
            usuario= redirect(url_for('index'))#para crear una cookie y guardar los datos del Usuario
            usuario.set_cookie(json.dumps(dict(request.form.items())))#en el navegador
            return usuario


@app.route('/processSignup', methods=['GET', 'POST'])#probado funciona (sige en duda el que quede guardado en la db)
def processSignup():#terminar Nombre de cookie
       email= "'" + str(request.form['email']) + "'"

       _name= request.form['name']
       _email= request.form['email']
       _lastname= request.form['surname']
       _password= request.form['contr']

       sql_search= "SELECT email_user FROM users WHERE email_user ={}".format(email)
       sql_insert= "INSERT INTO users (name_user, email_user, password_user, lastname_user) VALUES(%s,%s,%s,%s)"

       datos= (str(_name), email, str(_password), str(_lastname))

       row= search_data (sql_search)
       if row is None:
          insert_data(sql_insert, datos)
          usuario= redirect(url_for('index'))#para crear una cookie y guardar los datos del Usuario
          usuario.set_cookie("User", json.dumps(dict(request.form.items())))#en el navegador
          return usuario
       else:
          return redirect(url_for('index'))

@app.route('/processSignUpdate', methods=['GET', 'POST'])                       #(((Up Date del usuario)))
def processSignUpdate():#terminar
    #datos de la cookie

    _passwordN= request.form['password']

    sql_search= "SELECT email_user, password_user FROM users WHERE email_user ={} AND password_user ={}".format(_email, _password)
    sql_update= "UPDATE users SET columna1 = 'valor nuevo' WHERE columna2 = 'valor nuevo'"

@app.route('/processSignupRef', methods=['GET', 'POST'])
def processSignupRef(): #(usar las funciones de search_data y insert_data) _address= request.form['']
    #image = request.files['img']

    email= "'" + str(request.form['emailRef']) + "'"

    _name= request.form['nameRef']
    _email= request.form['emailRef']
    _password= request.form['contrRef']
    _department= request.form['departamento']
    _city= request.form['ciudad']
    _neighborhood= request.form['barrio']
    _address= request.form['direccion']
    _description= request.form['descripcion']
    _phone= request.form['telcontactoFijo']
    _celphone= request.form['telcontacto']
    _web= request.form['url']
    #_photo= Image.open(image)
    _type= None

    if request.form['gatos'] ==True:
        _type= ("Gatos ")
    if request.form['perros'] ==True:
        _type= _type + ("Perro ")
    if request.form['otrosAceptados'] != None:
        _type= _type + (str (request.form['otrosAceptados']))

    datos= (str(_name), str(_email), str(_password), str(_department), str(_city), str(_neighborhood), str(_address), str(_description), str(_phone), str(_celphone), str(_web), _photo, str(_type) )

    sql_search= "SELECT email_refuge FROM refuges WHERE email_refuge ={}".format(email)
    sql_insert= "INSERT INTO refuges (name_refuge, email_refuge, password_refuge, department_refuge, city_refuge, neighborhood_refuge, Googlemaps_refuge, description_refuge, phone_refuge, cellphone_refuge, website_refuge, image_refuge, animal_refuge) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    row= search_data(sql_search)
    if row is None:
       insert_data(sql_insert, datos)
       usuario= redirect(url_for('index'))#para crear una cookie y guardar los datos del Usuario
       usuario.set_cookie("User", json.dumps(dict(request.form.items())))#en el navegador
       return usuario
    else:
       return redirect(url_for('index'))

@app.route('/processSignupRefUpdate', methods=['GET', 'POST'])                  #(((Up Date del refugio)))
def processSignupRefUpdate():#terminar
    #datos de la cookie

    _passwordN= request.form['password']

    sql_search= "SELECT email_user, password_user FROM users WHERE email_user ={} AND password_user ={}".format(_email, _password)
    sql_update= "UPDATE users SET columna1 = 'valor nuevo' WHERE columna2 = 'valor nuevo'"

@app.route('/insertPet', methods=['GET', 'POST'])
def insert_Pet():#Terminar (enlases al formulario) probar
    image = request.files['img']

    _name= request.form['']
    _age= request.form['']
    _race= request.form['']
    _gender= request.form['']
    _health= request.form['']
    _coment= request.form['']
    _photo= Image.open(image)
    _type= None

    if request.form[''] == True:
        _type= ("Gato ")
    if request.form[''] == True:
        _type= _type + ("Perro")
    if request.form[''] != None:
        _type= _type + (str (request.form['']))

    datos= (str(_name), str(_age), str(_race), str(_gender), str(_health), str(_coment), str(_type), _photo)

    sql_insert= "INSERT INTO animals (name_animal, age_animal, breed_animal, gender_animal, health_animal, coments_animal, type_animal, photo_animal) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

    insert_data(sql_insert,datos)

    return redirect(url_for('index'))

@app.route('/searchCat', methods=['GET', 'POST'])                               #(((Boton de busqueda para "Gatos")))
def search_Cat():#Terminar pasar dato a el index ()
    sql_search= "SELECT type_animal, breed_animal FROM animals WHERE type_animal= Gato" #revisar si Gato tiene que ser str

    conexion = psycopg2.connect(host="animalicis.crl39vc3ngno.us-east-2.rds.amazonaws.com", database="animalicis", user="postgres", password="Perros2012")
    cur= conexion.cursor()
    cur.execute(sql_search)
    row= cur.fetchone()
    conexion.close()
    return redirect(url_for('index'))#agregar el row con los nombres de las razas existentes

@app.route('/searchDog', methods=['GET', 'POST'])                               #(((Boton de busqueda para "Perro")))
def search_Dog():#Terminar pasar dato a el index()
    sql_search= "SELECT type_animal, breed_animal FROM animals WHERE type_animal= Perro"

    conexion = psycopg2.connect(host="animalicis.crl39vc3ngno.us-east-2.rds.amazonaws.com", database="animalicis", user="postgres", password="Perros2012")
    cur= conexion.cursor()
    cur.execute(sql_search)
    row= cur.fetchone()
    conexion.close()
    return redirect(url_for('index'))#agregar el row con los nombres de las razas existentes

@app.route('/searchOther', methods=['GET', 'POST'])                             #(((Boton de busqueda para "Otros")))
def search_Other():#Terminar pasar dato a el index()
    sql_search= "SELECT type_animal, breed_animal FROM animals WHERE type_animal= Otro"

    conexion = psycopg2.connect(host="animalicis.crl39vc3ngno.us-east-2.rds.amazonaws.com", database="animalicis", user="postgres", password="Perros2012")
    cur= conexion.cursor()
    cur.execute(sql_search)
    row= cur.fetchone()
    conexion.close()
    return redirect(url_for('index'))#agregar el row con los nombres de las razas existentes

@app.route('/searchPet', methods=['GET', 'POST'])                               #(((Boton de busqueda general)))
def search_Pet(): #terminar y testear prinsipalmente la foto
    #buscar como sacar el tipo de animal (dado por el index) _type
    _age= request.form['edad']
    _gender= request.form['sexo']
    _race= request.form['raza']

    sql_search= "SELECT * FROM animals WHERE type_animal ={} AND breed_animal ={} AND gender_animal ={} AND age_animal ={}".format(_type, _race, _gender, _age)

    search_data(sql_search)

    return redirect(url_for('index'))#pasar el raw con los datos de los animales a la funcion que muestra los datos

def insert_data(sql_insert, datos):
    sql= sql_insert
    data= datos

    conexion = psycopg2.connect(host="animalicis.crl39vc3ngno.us-east-2.rds.amazonaws.com", database="animalicis", user="postgres", password="Perros2012")
    cur= conexion.cursor()
    cur.execute(sql, data)
    cur.close()
    conexion.close()

def search_data(sql_search): #fijarse como rescatar datos de una funcion !!!!!
    sql= sql_search

    conexion = psycopg2.connect(host="animalicis.crl39vc3ngno.us-east-2.rds.amazonaws.com", database="animalicis", user="postgres", password="Perros2012")
    cur= conexion.cursor()
    cur.execute(sql)
    row= cur.fetchone()
    cur.close()
    conexion.close()
    return (row)

if __name__ == '__main__':
    app.run(debug=True)
