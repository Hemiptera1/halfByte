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
from PIL import Image
from flask import Flask, request, url_for, redirect, render_template, session
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="postgres",pw="Perros2012",url="animalicis.crl39vc3ngno.us-east-2.rds.amazonaws.com",db="animalicis")
IMA_F = './static/Photo/Ref'
IMG_ANIMALS = './static/Photo/Animals'

app.config['UPLOAD_FOLDER'] = IMA_F
app.config['UPLOAD_FOLDER1'] = IMG_ANIMALS
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

from tablas import db


from sqlalchemy import create_engine, select
from tablas import User_, Refuge_, Animals_

db.drop_all() #comentar cuando se terminen las pruebas
db.create_all()



@app.route('/', methods=['GET'])           #index con nombre de usuario
def index():

    if "name" in session:
        _name=session['name']
        _type=session['type']
    else:
        _name=""
        _type=""
    context={'Nombre': _name, 'Tipo':_type}
    return render_template('index.html', **context)

@app.route('/account', methods=['GET'])    #ruta a la seleccion de signup
def account():
    return render_template('cuentas.html')

@app.route('/profile', methods=['GET'])    #El voton al perfil tiene que apuntar a esta funcion
def profile():#Probar

    _email= session['email']
    _password= session['password']
    _type= session['type']

    if _type != "User":
        row= Refuge_.query.filter_by(email=_email, pw_hash=_password).first()
        email= "'" + _email + "'"
        sql_search="SELECT id, name, photo FROM Animals_ WHERE email ={}".format(email)
        engine = create_engine(DB_URL)
        data = engine.execute(sql_search).fetchall ()
        #animals= myanimal(ram)
        context={"Nombre":row.name, "data":map(json.dumps, data),
                "Email":row.email, "Departamento":row.department,
                "Ciudad":row.city, "Barrio":row.neighborhood,
                "Diereccion":row.Googlemaps, "Descripcion":row.description,
                "Representante":row.rep, "Telefono":row.phone,
                "Celular":row.celphone, "Web":row.website,
                "Animales":row.animal, "Abierto":row.time_o,
                "Cerrado":row.time_c, "Foto":row.photo}

        return render_template('perfilRef.html', **context)

    else:
        row= User_.query.filter_by(email=_email, pw_hash=_password).first()
        email= "'" + _email + "'"
        sql_search="SELECT id, name, photo FROM Animals_ WHERE email ={}".format(email)
        engine = create_engine(DB_URL)
        data = engine.execute(sql_search).fetchall ()
        #animals= myanimal(ram)
        context={"Nombre":row.name, "Apellido":row.lastname, "Email":row.email, "data":map(json.dumps, data)}

        return render_template('perfilUsuario.html', **context)

@app.route('/profileV', methods=['GET'])
def profileV(_email=""):#Probar
    _email= session['email']

    row= User_.query.filter_by(email=_email).first()
    if row != None:
        email= "'" + _email + "'"
        sql_search="SELECT id, name, photo FROM Animals_ WHERE email ={}".format(email)
        engine = create_engine(DB_URL)
        data = engine.execute(sql_search).fetchall ()
        #animals= myanimal(ram)
        context={"Nombre":row.name, "Apellido":row.lastname, "Email":row.email, "data":map(json.dumps, data)}
    else:
        return redirect(url_for('index'))

    return render_template('perfilUsuarioV.html', **context)

@app.route('/profileRefV', methods=['GET']) #cuando se elige un animal resive un correo y debuelve los datos para el perfil visible
def profileRefV(_email=""):#Probar
    _email= session['email']

    row= Refuge_.query.filter_by(email=_email).first()
    if row != None:
        email= "'" + _email + "'"
        sql_search="SELECT id, name, photo FROM Animals_ WHERE email ={}".format(email)
        engine = create_engine(DB_URL)
        data = engine.execute(sql_search).fetchall ()
        #animals= myanimal(ram)

        context={"Nombre":row.name, "data":map(json.dumps, data),
                "Email":row.email, "Departamento":row.department,
                "Ciudad":row.city, "Barrio":row.neighborhood,
                "Diereccion":row.Googlemaps, "Descripcion":row.description,
                "Representante":row.rep, "Telefono":row.phone,
                "Celular":row.celphone, "Web":row.web,
                "Animales":row.animal, "Abierto":row.time_o,
                "Cerrado":row.time_c, "Foto":row.photo}
    else:
        return redirect(url_for('profileV'))

    return render_template('perfilRef.html', **context)

@app.route('/signup', methods=['GET'])      #ruta al signup
def signup():
    return render_template('signup.html')

@app.route('/signupRef', methods=['GET'])   #ruta al signupRef
def signupRef():
    return render_template('SignupRef.html')

@app.route('/signupAnimal', methods=['GET']) #ruta al registro de animales
def signupAnimal():
    return render_template('registroAnimales.html')

@app.route('/operation', methods=['GET'])   #ruta a "cono funciona la pagina"
def operation():
    return render_template('comoFunciona.html')

@app.route('/perfilAnimal', methods=['GET'])   # Ruta => "Perfil de animal"
def perfilAnimal():
    return render_template('perfilAnimal.html')


@app.route('/processLogin', methods=['GET', 'POST'])  #proceso de login
def processLogin():
        _email= str(request.args.get('email', None))
        _password= str(request.args.get('contraseña', None))

        row= Refuge_.query.filter_by(email=_email, pw_hash=_password).first()
        if row is None:
            row= User_.query.filter_by(email=_email, pw_hash=_password).first()
            if row is None:
                return  "Correo y/o contraceña incorrecta"
            else:
                usuario= redirect(url_for('profile'))
                session['email']= row.email
                session['password']= row.pw_hash
                session['name']= row.name
                session['type']= "User"
                #usuario.set_cookie("User", json.dumps({'email':row.email, 'password':row.pw_hash, 'name':row.name}))#en el navegador
                return usuario
        else:
            session['email']= row.email
            session['password']= row.pw_hash
            session['name']= row.name
            session['type']= "Refuge"
            return redirect(url_for('profile'))

@app.route('/processSignup', methods=['GET', 'POST']) #proceso de registro de Usuario
def processSignup():

       _name= request.form['name']
       _email= request.form['email']
       _lastname= request.form['surname']
       _password= request.form['contr']

       row= User_.query.filter_by(email=_email).first()
       if row is None:
           row= Refuge_.query.filter_by(email=_email, pw_hash=_password).first()
           if row is None:
               intro= User_(name= _name, lastname=_lastname, email=_email, pw_hash=_password)
               db.session.add(intro)
               db.session.commit()

               usuario= redirect(url_for('index'))#para crear una cookie y guardar los datos del Usuario
               session['email']= _email
               session['password']= _password
               session['name']= _name + " " + _lastname
               session['type']= "User"
               #usuario.set_cookie("User", json.dumps({'email':_email, 'password':_password, 'name':_name + " " + _lastname}))#en el navegador
               return usuario
           else:
               return "la cuenta ya existe" #redirect(url_for('index')) #esa cuenta ya existe
       else:
           return "la cuenta ya existe"

@app.route('/processSignUpdate', methods=['GET', 'POST']) #proceso de actualizacion de datos del Ususario
def processSignUpdate():#Probar
    #data= json.loads(request.cookies.get('User'))
    #ty= data.get('email')

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
    session['email']= request.form['email']
    session['password']= request.form['contr']
    session['name']= request.form['name'] + " " + request.form['surname']
    session['type']= "User"
    #usuario.set_cookie("User", json.dumps({'email': request.form['email'], 'password': request.form['contr'], 'name':request.form['name']}))#en el navegador
    return usuario

@app.route('/processSignupRef', methods=['GET', 'POST']) #proceso de registri de Refugios
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

    #if photo !=None:
    _photo= IMA_F + "/" + _email + ".jpg"

    img=Image.open(photo)  #reparar el error de cunado photo no tiene imagen !!!!!
    img.save(_photo)
    #else:
        #_photo= IMA_F + "/base.jpg"
        #img=Image.open(_photo)

    if request.form['gatos'] == 'gatos': #reparar
        _type= "Gatos "
    if request.args.get('perros') == 'perros':
        _type= _type + "Perro "
    if request.form['otrosAceptados'] != None:
        _type= _type + str (request.form['otrosAceptados'])


    row= Refuge_.query.filter_by(email=_email).first()
    if row is None:
        row= User_.query.filter_by(email=_email).first()
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
                   session['email']= _email
                   session['password']= _password
                   session['name']= _name
                   session['type']= "Refuge"
                   #usuario.set_cookie("User", json.dumps({'email': _email, 'password': _password, 'name':_name}))#en el navegador
                   return usuario
        else:
           return "la cuenta ya existe" #redirect(url_for('index'))
    else:
       return "la cuenta ya existe"

@app.route('/processSignupRefUpdate', methods=['GET', 'POST']) #proceso de actualizacion de datos del Refugio
def processSignupRefUpdate():#terminar Copiar el up data de user


    sess.query(Refuge_).filter(Refuge_.pw_hasha ==request.form['contr']).\
    update({Refuge_.pw_hasha: request.form['contr']}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.email ==request.form['email']).\
    update({Refuge_.email: request.form['email']}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.name ==request.form['name']).\
    update({Refuge_.name: request.form['name']}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.department ==request.form['Departamento']).\
    update({Refuge_.department: request.form['Departamento']}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.city ==request.form['ciudad']).\
    update({Refuge_.city: request.form['ciudad']}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.neighborhood ==request.form['barrio']).\
    update({Refuge_.neighborhood: request.form['barrio']}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.Googlemaps ==request.form['direccion']).\
    update({Refuge_.Googlemaps: request.form['direccion']}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.description ==request.form['descripcion']).\
    update({Refuge_.description: request.form['descripcion']}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.rep ==request.form['responsableContacto']).\
    update({Refuge_.rep: request.form['responsableContacto']}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.phone ==request.form['telcontactoFijo']).\
    update({Refuge_.phone: request.form['telcontactoFijo']}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.celphone ==request.form['telcontacto']).\
    update({Refuge_.celphone: request.form['telcontacto']}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.website ==request.form['url']).\
    update({Refuge_.website: request.form['url']}, synchronize_session=False)

    if request.form['gatos'] == 'gatos': #reparar
        _type= "Gatos "
    if request.args.get('perros') == 'perros':
        _type= _type + "Perro "
    if request.form['otrosAceptados'] != None:
        _type= _type + str (request.form['otrosAceptados'])

    sess.query(Refuge_).filter(Refuge_.animal ==_type).\
    update({Refuge_.animal: _type}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.time_o ==request.form['horaInicio']).\
    update({Refuge_.time_o: request.form['horaInicio']}, synchronize_session=False)

    sess.query(Refuge_).filter(Refuge_.time_c ==request.form['horaFinal']).\
    update({Refuge_.time_c: request.form['horaFinal']}, synchronize_session=False)

    photo= request.files['img']

    if photo != None:
        os.remove(IMA_F + "/" + session['email'] + ".jpg")
        _photo= IMA_F + "/" + request.form['email'] + ".jpg"
        img=Image.open(photo)
        img.save(_photo)

    usuario= redirect(url_for('index'))#para crear una cookie y guardar los datos del Usuario
    session['email']= request.form['email']
    session['password']= request.form['contr']
    session['name']= request.form['name'] + " " + request.form['surname']
    session['type']= "Refuge"

@app.route('/insertPet', methods=['GET', 'POST']) #proceso de registro de animales
def insert_Pet():#Terminar (enlases al formulario) probar
    #data= json.loads(request.cookies.get('User')) #recordar si el enlace esta para no registrados poner un try
    ty= session['email']

    image = request.files['img']

    _name= request.form['name']
    _age= request.form['edad']
    _race= request.form['raza']
    _gender= request.form['genero']
    _coment= request.form['comentarios']
    _type= request.form['especie']

    if request.form['castracion'] == "Castrado":
        _health= "Esta Castrado"
    else:
        _health= "No esta Castrado"

    if request.form['enfermedades'] != "No":
        _health+= "Está " + request.form['enfermedades']



    image_a= os.listdir(IMG_ANIMALS)
    if image_a == []:
        _id = 0
    else:
        _id = 1 + int(image_a[-1])

    _photo= IMG_ANIMALS + "/" + str(_id) + ".jpg"

    img=Image.open(image)
    img.save(_photo)

    intro=Animals_(email=ty, name=_name, age=_age,
                   breed=_race, gender=_gender,
                   health=_health, coments=_coment,
                   type=_type, id=_id, photo=_photo)

    db.session.add(intro)
    db.session.commit()
    context={"confirmacion":"Su mascota fue registrada con exito"}
    return redirect(url_for('signupAnimal'))

@app.route('/insertPet_Update', methods=['GET', 'POST'])  #FALTA proceso de actualizacion de datos del Refugio
def insertPet_Update():
    sess.query(User_).filter(User_.pw_hasha ==request.form['contr']).\
    update({User_.pw_hasha: request.form['contr']}, synchronize_session=False)
    sess.query(User_).filter(User_.email ==request.form['email']).\
    update({User_.email: request.form['email']}, synchronize_session=False)
    sess.query(User_).filter(User_.name ==request.form['name']).\
    update({User_.name: request.form['name']}, synchronize_session=False)
    sess.query(User_).filter(User_.lastname ==request.form['surname']).\
    update({User_.lastname: request.form['surname']}, synchronize_session=False)

    usuario= redirect(url_for('index'))#para crear una cookie y guardar los datos del Usuario
    session['email']= request.form['email']
    session['password']= request.form['contr']
    session['name']= request.form['name'] + " " + request.form['surname']
    session['type']= "User"


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

@app.route('/searchRef', methods=['GET', 'POST'])  #buscador de refugios por barrio o ciudad
def searchRef():

    if request.form['direccion'] != None:
        _address= "==" + "'" + str (request.args.get('direccion')) + "'"
    else:
        _address= "<>" + "'" + str (request.args.get('direccion')) + "'"

    _type= request.args.get('tipo')

    sql_search= """SELECT email, name, description, animal, photo
                   WHERE animal={animal} department{add} OR city {add} OR neighborhood {add}""".format(animal=_type,add=_address)

    engine = create_engine(DB_URL)
    data = engine.execute(sql_search).fetchall()



    return render_template(busqueda.html, data=map(json.dumps, data))

@app.route('/searchPet', methods=['GET', 'POST'])    #(((Boton de busqueda general)))
def search_Pet(): #terminar y testear prinsipalmente la foto #puedo usar el metodo Animals_.query.slice(self, start, stop)

    intro= Animals_(name= 'Sonriente', age='Joven', email='emiliano.garin333@gmail.com', breed='Pelo corto', gender='Macho' , health='si', coments='sonrie', type='Gato', photo="X")
    intro1= Animals_(name= 'Felix', age='Joven', email='emiliano.garin333@gmail.com', breed='Persa', gender='Macho' , health='si', coments='sonrie', type='Gato', photo="X")
    intro2= Animals_(name= 'Blair', age='Joven', email='emiliano.garin333@gmail.com', breed='Bombai', gender='Hembra' , health='si', coments='sonrie', type='Gato', photo="X")
    intro3= Animals_(name= 'Makise', age='Joven', email='emiliano.garin333@gmail.com', breed='Bombai', gender='Hembra' , health='si', coments='sonrie', type='Gato', photo="X")

    intro4= Animals_(name= 'Rex', age='Adulto', email='emiliano.garin333@gmail.com', breed='Labrador Retriever', gender='Macho' , health='si', coments='sonrie', type='Perro', photo="X")
    intro5= Animals_(name= 'Roy', age='Joven', email='emiliano.garin333@gmail.com', breed='Golden Retriever', gender='Macho' , health='si', coments='sonrie', type='Perro', photo="X")
    intro6= Animals_(name= 'Cometa', age='Adulto', email='emiliano.garin333@gmail.com', breed='Bulldog', gender='Hembra' , health='si', coments='sonrie', type='Perro', photo="X")
    intro7= Animals_(name= 'Lssi', age='Joven', email='emiliano.garin333@gmail.com', breed='Rooweiler', gender='Hembra' , health='si', coments='sonrie', type='Perro', photo="X")

    intro8= Animals_(name= 'Donatelo', age='Adulto', email='emiliano.garin333@gmail.com', breed='Tortuga', gender='Macho' , health='si', coments='sonrie', type='Otro', photo="X")
    intro9= Animals_(name= 'Fliper', age='Joven', email='emiliano.garin333@gmail.com', breed='pez', gender='Macho' , health='si', coments='sonrie', type='Otro', photo="X")
    intro10= Animals_(name= 'Sardinilla', age='Adulto', email='emiliano.garin333@gmail.com', breed='Caballo', gender='Hembra' , health='si', coments='sonrie', type='Otro', photo="X")
    intro11= Animals_(name= 'Akame', age='Joven', email='emiliano.garin333@gmail.com', breed='Pajaro', gender='Hembra' , health='si', coments='sonrie', type='Otro', photo="X")

    db.session.add(intro)
    db.session.add(intro1)
    db.session.add(intro2)
    db.session.add(intro3)
    db.session.add(intro4)
    db.session.add(intro5)
    db.session.add(intro6)
    db.session.add(intro7)
    db.session.add(intro8)
    db.session.add(intro9)
    db.session.add(intro10)
    db.session.add(intro11)
    db.session.commit()


    if request.args.get('Edad') != "F":#poner el valor real
        _age= "= " + "'" + str (request.args.get('Edad')) + "'"
    else:
        _age= "<> " + "'" + str (request.args.get('Edad')) + "'"

    #return "no Falla {}".format(_age)
    if request.args.get('Sexo') != "O":#poner el valor real
        _gender=  "= " + "'" + str (request.args.get('Sexo')) + "'"
    else:
        _gender= "<> " + "'" + str (request.args.get('Sexo')) + "'"

    #return "no Falla {}".format(_gender)
    if request.args.get('Raza') != "R":#poner el valor real
        _race= "= " + "'" + str (request.args.get('Raza')) + "'"
    else:
        _race= "<> " + "'" + str (request.args.get('Raza')) + "'"

    #return "no Falla {}".format(_race)

    if request.args.get('Animal') == "Gato":
        _type= "= " + "'" + "Gato" + "'"
    elif request.args.get('Animal') == "Perro":
        _type= "= " + "'" + "Perro" + "'"
    elif request.args.get('Animal') == "Otro":
        _type= "= " + "'" + "Otro" + "'"
    else:
        _type= "<> " + "'" + "" + "'" #comentar despues
    #return "no Falla {}".format(_type)

    if request.args.get('direccion') != "":
        _address= "=" + "'" + str (request.args.get('direccion')) + "'"
    else:
        _address= "<>" + "'" + str (request.args.get('direccion')) + "'"

    #return "no Falla {}".format(_address)
    data= {'_type':_type, '_race':_race, '_gender':_gender, '_age':_age, 'add':_address}

    #sql_search= "SELECT email, name, age, breed, gender, health, coments, type, photo FROM Animals_ WHERE type {} AND breed {} AND gender {} AND age {}".format(_type, _race, _gender, _age)

    sql_search= """SELECT Animals_.email, Animals_.name, age, breed, gender, health, coments, type, Animals_.photo
                   FROM Animals_ JOIN Refuge_ ON Animals_.email=Refuge_.email
                   WHERE Animals_.type {_type} AND Animals_.breed {_race} AND
                   Animals_.gender {_gender} AND Animals_.age {_age} AND
                   (Refuge_.department{add} OR Refuge_.city {add} OR Refuge_.neighborhood {add})""".format(**data)

    #if request.args.get('Otro') == "Otro":
    #    _type1= "'" + "Gato" + "'"
    #    _type2= "'" + "Perro" + "'"
    #    sql_search= "SELECT email, name, eag, breed, gender, health, coments, type, photo FROM Animals_ WHERE type <>{} AND type <>{} AND breed {} AND gender {} AND age {}".format(_type1, _type2, _race, _gender, _age)

    engine = create_engine(DB_URL)
    row = engine.execute(sql_search).fetchall ()
    data =  file_animal(row)
    return (data)
    #return render_template('busqueda.html', data=map(json.dumps, data))


def file_Ref(row):#ajustar
    row=row
    cantidad=[0,1,2,3,4,5]
    ficha=""
    try:
        data= json.loads(request.cookies.get('Fichero'))
    except TypeError:
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
            _coments= row[cont][2]
            _animal= row[cont][3]
            _photo= row[cont][4]

            ficha +="""Email={} Nombre={} Comentario={} Animales={} Foto{}""".format(_email,_name, _coments, _animal, _photo)
            cont +=1

    return ficha

def file_animal(row):#agregar el codigo HTML que forma la ficha
    row=row
    cantidad=[0,1,2,3,4,5]
    ficha=[]
    try:
        data= json.loads(request.cookies.get('Fichero'))
    except TypeError:
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
            _age= row[cont][2]
            _breed= row[cont][3]
            _gender= row[cont][4]
            _health= row[cont][5]
            _coments= row[cont][6]
            _type= row[cont][7]
            _photo= row[cont][8]

            ficha.append({'email':_email, 'name':_name, 'age':_age, 'breed':_breed,
                          'gender':_gender, 'health':_health, 'coments':_coments,
                          'type':_type, 'photo':_photo})
            #ficha += """Animal {} [[[email = {}, name= {}, eag= {}, breed= {}, gender= {}, health= {}, coments= {}, _type={}, _photo={}]]]                """.format(cont,_email,_name,_age,_breed,_gender,_health,_coments,_type,_photo)
            cont +=1

    return ficha

def myanimal(row):#agregar el codigo HTML que forma la ficha
    row=row
    cantidad=[0,1,2,3,4,5]
    ficha=""
    try:
        data= json.loads(request.cookies.get('MyAnilal'))
    except TypeError:
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
    return ficha


if __name__ == '__main__':
    app.run(debug=True)
