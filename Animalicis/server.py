# 1)Autenticación de formularios (Signup, login) (pendiente de probar)
# 2)conectar liks de barra de tareas (en proceso)
# 3)Autenticación filtro de sección de adopcion (en proceso)
# 4)Visualización de animales disponibles para adopción (en proceso)
# 5)Conectar formularios a base de datos (en simultaneo)
# 6)Mapa de refugios (pospuesto)
# 7)Listados de eventos (pendiente)

import json
import psycopg2
import config
import os
from flask import Flask, request, url_for, redirect
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy #por algun otibo no reconose el proseso create_engine

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="postgres",pw="Perros2012",url="animalicis.crl39vc3ngno.us-east-2.rds.amazonaws.com",db="animalicis")
IMA_F = './data/Photo/Ref'
IMG_ANIMALS = './data/Photo/Animals'

app.config['UPLOAD_FOLDER'] = IMA_F
app.config['UPLOAD_FOLDER1'] = IMG_ANIMALS
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from tablas import db
db.drop_all()              #¡¡¡¡¡borrar cuando deje de modificar las tablas!!!!
db.create_all()

from sqlalchemy import create_engine, select
from tablas import User_, Refuge_, Animals_


@app.route('/', methods=['GET'])
def index():#poner el **context y el 'Nomgre' en el html
    _name=""
    try:
        data= json.load(request.cookies.get('User'))
    except AttributeError:
        data= {}
    else:
        _name= data.get('name')
    context={'Nombre': _name}
    return app.send_static_file('index.html') #falta conectar la bariable

@app.route('/account', methods=['GET'])
def account():
    return app.send_static_file('cuentas.html')

@app.route('/profile', methods=['GET'])    #poner el **context
def profile():#Probar
    data= json.load(request.cookis.get('User'))
    _email= data.get('email')
    _password= data.get('password')

    row= User_.query.filter_by(email=_email, pw_hash=_password).first()
    if row != None:
        email= "'" + _email + "'"
        sql_search="SELECT id, name, photo FROM Animals_ WHERE email ={}".format(email)
        engine = create_engine(DB_URL)
        ram = engine.execute(sql_search).fetchall ()
        animals= myanimal(ram)
        context={"Nombre":row.name, "Apellido":row.lastname, "Email":row.email, "miAnimal":animals}
    else:
        return app.send_static_file('index.html')

    return app.send_static_file('perfilUsuario.html')

@app.route('/profileV', methods=['GET', ]) #poner el **context
def profileV(_email=""):#Probar

    row= User.query.filter_by(email=_email).first()
    if row != None:
        email= "'" + _email + "'"
        sql_search="SELECT id, name, photo FROM Animals_ WHERE email ={}".format(email)
        engine = create_engine(DB_URL)
        ram = engine.execute(sql_search).fetchall ()
        animals= myanimal(ram)
        context={"Nombre":row.name, "Apellido":row.lastname, "Email":row.email, "miAnimal":animals}
    else:
        return app.send_static_file('index.html')

    return app.send_static_file('perfilUsuarioV.html')

@app.route('/profileRef', methods=['GET']) #poner el **context
def profile():#Probar
    data= json.load(request.cookis.get('User'))
    _email= data.get('email')
    _password= data.get('password')

    row= Refuge_.query.filter_by(email=_email, pw_hash=_password).first()
    if row != None:
        email= "'" + _email + "'"
        sql_search="SELECT id, name, photo FROM Animals_ WHERE email ={}".format(email)
        engine = create_engine(DB_URL)
        ram = engine.execute(sql_search).fetchall ()
        animals= myanimal(ram)
        context={"Nombre":row.name,"miAnimal":animals,
                "Email":row.email, "Departamento":row.department,
                "Ciudad":row.city, "Barrio":row.neighborhood,
                "Diereccion":row.Googlemaps, "Descripcion":row.description,
                "Representante":row.rep, "Telefono":row.phone,
                "Celular":row.celphone, "Web":row.web,
                "Animales":row.animal, "Abierto":row.time_o,
                "Cerrado":row.time_c, "Foto":row.photo}
    else:
        return app.send_static_file('index.html')

    return app.send_static_file('perfilRef.html')

@app.route('/profileRefV', methods=['GET']) #poner el **context
def profile(_email=""):#Probar

    row= Refuge_.query.filter_by(email=_email).first()
    if row != None:
        email= "'" + _email + "'"
        sql_search="SELECT id, name, photo FROM Animals_ WHERE email ={}".format(email)
        engine = create_engine(DB_URL)
        ram = engine.execute(sql_search).fetchall ()
        animals= myanimal(ram)
        context={"Nombre":row.name,"miAnimal":animals,
                "Email":row.email, "Departamento":row.department,
                "Ciudad":row.city, "Barrio":row.neighborhood,
                "Diereccion":row.Googlemaps, "Descripcion":row.description,
                "Representante":row.rep, "Telefono":row.phone,
                "Celular":row.celphone, "Web":row.web,
                "Animales":row.animal, "Abierto":row.time_o,
                "Cerrado":row.time_c, "Foto":row.photo}
    else:
        return app.send_static_file('index.html')

    return app.send_static_file('perfilRef.html')

@app.route('/signup', methods=['GET'])
def signup():
    return app.send_static_file('signup.html')

@app.route('/signupRef', methods=['GET'])
def signupRef():
    return app.send_static_file('SignupRef.html')


@app.route('/processLogin', methods=['GET', 'POST'])
def processLogin():
        _email= str(request.args.get('email', None))
        _password= str(request.args.get('contraseña', None))


        row= Refuge_.query.filter_by(email=_email, pw_hash=_password).first()
        if row is None:
            row= User_.query.filter_by(email=_email, pw_hash=_password).first()
            if row is None:
                return  "Correo y/o contraceña incorrecta"

        usuario= redirect(url_for('index'))#para crear una cookie y guardar los datos del Usuario
        usuario.set_cookie("User", json.dumps({'email':row.email, 'password':row.pw_hash, 'name':row.name}))#en el navegador
        return usuario

@app.route('/processSignup', methods=['GET', 'POST'])
def processSignup():

       _name= str(request.form['name'])
       _email= str(request.form['email'])
       _lastname= str(request.form['surname'])
       _password= str(request.form['contr'])

       row= User_.query.filter_by(email=_email).first()
       if row is None:
           intro= User_(name= _name, lastname=_lastname, email=_email, pw_hash=_password)
           db.session.add(intro)
           db.session.commit()

           usuario= redirect(url_for('index'))#para crear una cookie y guardar los datos del Usuario
           usuario.set_cookie("User", json.dumps({'email':row.email, 'password':row.pw_hash, 'name':row.name}))#en el navegador
           return usuario
       else:
           return redirect(url_for('index'))

@app.route('/processSignUpdate', methods=['GET', 'POST'])
def processSignUpdate():#Probar
    data= json.load(request.cookis.get('User'))
    ty= data.get('email')

    #_passwordN= "'" + str(request.form['contr']) + "'"

    #sql_update= "UPDATE users SET columna1 = 'valor nuevo' WHERE columna2 = 'valor nuevo'"


    sess.query(User_).filter(User_.pw_hasha ==request.form['contr']).\
    update({User_.pw_hasha: request.form['contr']}, synchronize_session=False)
    sess.query(User_).filter(User_.email ==request.form['email']).\
    update({User_.email: request.form['email']}, synchronize_session=False)
    sess.query(User_).filter(User_.name ==request.form['name']).\
    update({User_.name: request.form['name']}, synchronize_session=False)
    sess.query(User_).filter(User_.lastname ==request.form['surname']).\
    update({User_.lastname: request.form['surname']}, synchronize_session=False)

    usuario= redirect(url_for('index'))#para crear una cookie y guardar los datos del Usuario
    usuario.set_cookie("User", json.dumps({'email': request.form['email'], 'password': request.form['contr'], 'name':request.form['name']}))#en el navegador
    return usuario

@app.route('/processSignupRef', methods=['GET', 'POST'])
def processSignupRef(): #Probar el funcionamiento de la imagen
    photo= request.files['img']

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
    _rep=  request.form['responsableContacto']
    _time_o= request.form['horaInicio']
    _time_c= request.form['horaFinal']
    _type= ""

    email= " " + _email

    photo.save(os.path.join(app.config['UPLOAD_FOLDER'], email))
    _photo= os.getcwd() + "\ " +  _email


    if request.form['gatos'] == 'gatos': #reparar
        _type= "Gatos "
    if request.args.get('perros') == 'perros':
        _type= _type + "Perro "
    if request.form['otrosAceptados'] != None:
        _type= _type + str (request.form['otrosAceptados'])


    row= Refuge_.query.filter_by(email=_email).first()
    if row is None:
       intro= Refuge_(name= _name, email= _email,
                      pw_hash= _password, department= _department,
                      city=_city, neighborhood=_neighborhood,
                      Googlemaps=_address, description=_description,
                      phone=_phone, celphone=_celphone,
                      website=_web, animal=_type,
                      time_o=_time_o, time_c=_time_c,
                      rep=_rep, photo=_photo)
       db.session.add(intro)
       db.session.commit()

       usuario= redirect(url_for('index'))#para crear una cookie y guardar los datos del Usuario
       usuario.set_cookie("User", json.dumps({'email': _email, 'password': _password, 'name':_name}))#en el navegador
       return usuario
    else:
       usuario= redirect(url_for('index'))#para crear una cookie y guardar los datos del Usuario
       usuario.set_cookie("User", json.dumps({'email':row.email, 'password':row.pw_hash, 'name':row.name}))#en el navegador
       return usuario

@app.route('/processSignupRefUpdate', methods=['GET', 'POST'])
def processSignupRefUpdate():#terminar Copiar el up data de user
    #datos de la cookie

    _passwordN= request.form['password']

    sql_search= "SELECT email_user, password_user FROM users WHERE email_user ={} AND password_user ={}".format(_email, _password)
    sql_update= "UPDATE users SET columna1 = 'valor nuevo' WHERE columna2 = 'valor nuevo'"

@app.route('/insertPet', methods=['GET', 'POST'])
def insert_Pet():#Terminar (enlases al formulario) probar
    data= json.load(request.cookis.get('User'))
    ty= data.get('email')

    image = request.files['img']

    _name= request.form['']
    _age= request.form['']
    _race= request.form['']
    _gender= request.form['']
    _health= request.form['']
    _coment= request.form['']
    _type= ""

    if request.form[''] == True:
        _type= ("Gato ")
    if request.form[''] == True:
        _type= _type + ("Perro ")
    if request.form[''] != None:
        _type= _type + (str (request.form['']))

    image_a= os.listdir(IMG_ANIMALS)
    if image_a == None:
        _id = 0
    else:
        _id = 1 + int(image_a[-1])

    id_= " " + str(_id)

    image.save(os.path.join(app.config['UPLOAD_FOLDER1'], id_))
    _photo= os.getcwd() + "\ " +  str(_id)

    intro=Animals_(email=ty, name=_name, age=_age,
                   breed=_race, gender=_gender,
                   health=_health, coments=_coment,
                   type=_type, id=_id, photo=_photo)

    db.session.add(intro)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/searchCat', methods=['GET', 'POST'])              #eliminar
def search_Cat():#Terminar pasar dato a el index ()
    animal= "'" + "Gato" + "'"
    sql_search= "SELECT DISTINCT * FROM Animals_ WHERE type= {}".format(animal) #revisar si Gato tiene que ser str

    intro= Animals_(name= 'Sonriente', eag='j', email='_email', breed='Pelo corto', gender='Macho' , health='si', coments='sonrie', type='Gato')
    intro1= Animals_(name= 'Felix', eag='j', email='_email', breed='Persa', gender='Macho' , health='si', coments='sonrie', type='Gato')
    intro2= Animals_(name= 'Blair', eag='j', email='_email', breed='Bombai', gender='Hembra' , health='si', coments='sonrie', type='Gato')
    intro3= Animals_(name= 'Makise', eag='j', email='_email', breed='Bombai', gender='Hembra' , health='si', coments='sonrie', type='Gato')
    db.session.add(intro)
    db.session.add(intro1)
    db.session.add(intro2)
    db.session.add(intro3)
    db.session.commit()

    engine = create_engine(DB_URL)
    message = engine.execute(sql_search).fetchall ()
    row= str(message)

    #usuario= redirect(url_for('index'))
    #usuario.set_cookie("Animal", json.dumps(row))
    #usuario.set_cookie("type", json.dumps({'type': 'Cat'}))
    return row

@app.route('/searchDog', methods=['GET', 'POST'])              #eliminar
def search_Dog():#Terminar pasar dato a el index()
    intro= Animals_(name= 'Sonriente', eag='j', email='_email', breed='Pelo corto', gender='Macho' , health='si', coments='sonrie', type='Gato')
    intro1= Animals_(name= 'Felix', eag='j', email='_email', breed='Persa', gender='Macho' , health='si', coments='sonrie', type='Gato')
    intro2= Animals_(name= 'Blair', eag='j', email='_email', breed='Bombai', gender='Hembra' , health='si', coments='sonrie', type='Gato')
    intro3= Animals_(name= 'Makise', eag='j', email='_email', breed='Bombai', gender='Hembra' , health='si', coments='sonrie', type='Gato')
    db.session.add(intro)
    db.session.add(intro1)
    db.session.add(intro2)
    db.session.add(intro3)
    db.session.commit()


    animal= "'" + "Perro" + "'"
    sql_search= "SELECT DISTINCT breed_animal FROM animals WHERE type_animal= {}".format(animal)

    row= search_data(sql_search)
    usuario= redirect(url_for('index'))
    usuario.set_cookie("Animal", json.dumps(row))
    usuario.set_cookie("type", json.dumps({'type': 'Dog'}))
    return usuario

@app.route('/searchOther', methods=['GET', 'POST'])            #eliminar
def search_Other():#Terminar pasar dato a el index()
    cat= "'" + "Gato" + "'"
    dog= "'" + "Perro" + "'"

    sql_search= "SELECT DISTINCT breed_animal FROM animals WHERE type_animal <> {} AND type_animal <> {}".format(cat, dog)

    row= search_data(sql_search)
    usuario= redirect(url_for('index'))
    usuario.set_cookie("Animal", json.dumps(row))
    usuario.set_cookie("type", json.dumps({'type': 'Other'}))
    return usuario

@app.route('/searchPet', methods=['GET', 'POST'])    #(((Boton de busqueda general)))
def search_Pet(): #terminar y testear prinsipalmente la foto #puedo usar el metodo Animals_.query.slice(self, start, stop)
    intro= Animals_(name= 'Sonriente', age='Joven', email='_email', breed='Pelo corto', gender='Macho' , health='si', coments='sonrie', type='Gato')
    intro1= Animals_(name= 'Felix', age='Joven', email='_email', breed='Persa', gender='Macho' , health='si', coments='sonrie', type='Gato')
    intro2= Animals_(name= 'Blair', age='Joven', email='_email', breed='Bombai', gender='Hembra' , health='si', coments='sonrie', type='Gato')
    intro3= Animals_(name= 'Makise', age='Adulto', email='_email', breed='Bombai', gender='Hembra' , health='si', coments='sonrie', type='Gato')
    intro4= Animals_(name= 'Makise', age='Adulto', email='_email', breed='Bombai', gender='Hembra' , health='si', coments='sonrie', type='Gato')
    db.session.add(intro4)
    db.session.add(intro)
    db.session.add(intro1)
    db.session.add(intro2)
    db.session.add(intro3)
    db.session.commit()

    if request.args.get('edad') != "F":
        _age= "= " + "'" + str (request.args.get('edad')) + "'"
    else:
        _age= "<> " + "'" + str (request.args.get('edad')) + "'"

    if request.args.get('sexo') == "R":
        _gender=  "= " + "'" + str (request.args.get('sexo')) + "'"
    else:
        _gender= "<> " + "'" + str (request.args.get('sexo')) + "'"

    if request.args.get('raza') == "O":
        _race= "= " + "'" + str (request.args.get('raza')) + "'"
    else:
        _race= "<> " + "'" + str (request.args.get('raza')) + "'"


    #if request.form['Ref'] == "Ref":
    #    _address= "'" + str (request.form['direccion']) + "'"
    #    sql_search=


    if request.args.get('Gato') == "Gato":
        _type= "'" + "Gato" + "'"
    elif request.args.get('Perro') == "Perro":
        _type= "'" + "Perro" + "'"

    sql_search= "SELECT email, name, age, breed, gender, health, coments, type FROM Animals_ WHERE type ={} AND breed {} AND gender {} AND age {}".format(_type, _race, _gender, _age)

    if request.args.get('Otro') == "Otro":
        _type1= "'" + "Gato" + "'"
        _type2= "'" + "Perro" + "'"
        sql_search= "SELECT email, name, eag, breed, gender, health, coments, type, photo FROM Animals_ WHERE type <>{} AND type <>{} AND breed {} AND gender {} AND age {}".format(_type1, _type2, _race, _gender, _age)

    engine = create_engine(DB_URL)
    row = engine.execute(sql_search).fetchall ()

    ficha=file_animal(row)

    context={'Ficha': ficha}

    return ficha


def file_animal(row):#agregar el codigo HTML que forma la ficha
    row=row
    cantidad=[0,1,2,3,4,5]
    ficha=""
    try:
        data= json.load(request.cookies.get('Fichero'))
    except AttributeError:
        data= {}
    else:
        cantidad= data.get('cant')


    for cont  in cantidad:
        try:
            _email= row[cont][0]
        except IndexError:
            break
        else:
            _name= row[cont][1]
            _eag= row[cont][2]
            _breed= row[cont][3]
            _gender= row[cont][4]
            _health= row[cont][5]
            _coments= row[cont][6]
            _type= row[cont][7]
            _photo= row[cont][8]

            ficha +="""email = {}, name= {}, eag= {}, breed= {}, gender= {}, health= {}, coments= {}, _type={}, _photo={}
                    """.format(_email,_name,_eag,_breed,_gender,_health,_coments,_type,_photo)
            cont +=1

    return ficha

def myanimal(row):#agregar el codigo HTML que forma la ficha
    row=row
    cantidad=[0,1,2,3,4,5]
    ficha=""
    try:
        data= json.load(request.cookies.get('MyAnilal'))
    except AttributeError:
        data= {}
    else:
        cantidad= data.get('cant')


    for cont  in cantidad:
        try:
            _id= row[cont][0]
        except IndexError:
            break
        else:
            _name=row[cont][1]
            _photo=row[cont][2]

            ficha="""id= {}, Nombre={}, Foto={}""".format(_id, _name, _photo)

            cont += 1
    return (ficha)


if __name__ == '__main__':
    app.run(debug=True)
