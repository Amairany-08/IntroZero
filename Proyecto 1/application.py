import os
from flask import Flask, render_template, request, session, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "cualquiera32"
app.permanent_session_lifetime=timedelta(minutes=60)
engine = create_engine("postgres://qoqkcosz:P41XZfuPw6OxY5Y48sBA6o2r6HAcypnc@balarama.db.elephantsql.com:5432/qoqkcosz")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        usuario = request.form.get("usuario")
        contrasena = request.form.get("contrasena")
        if(usuario and contrasena):
            usuarioB = db.execute("SELECT usuario,contrasena FROM usuarios WHERE usuario = :usuario",{"usuario": usuario}).fetchall()
            if(not usuarioB):
                 return render_template("index.html",error="Usuario no encontrado")
            elif(usuario == usuarioB[0][0] and contrasena == usuarioB[0][1]):
                session.permanent = True
                session['usuario'] = usuario
                return redirect('/busqueda')     
            else:
                return render_template("index.html",error="Contraseña Incorrecta")
        else:
            return render_template("index.html",error="Llene todos los campos")

    else:
        try:
            if(session['usuario']):
                return redirect('/busqueda')
        except:
            return render_template("index.html")

@app.route("/busqueda", methods=["GET","POST"])
def busqueda():
    if request.method == 'POST':
        busqueda = request.form.get('busqueda')
        libros = db.execute("SELECT * FROM libros WHERE isbn like :busqueda OR year like :busqueda OR title like :busqueda OR author like :busqueda",{"busqueda": "%"+busqueda.strip()+"%"}).fetchall()
        return render_template("busqueda.html",libros=libros)

    else:
        return render_template("busqueda.html")
@app.route("/libro/<book_isbn>", methods=["GET","POST"])
def libro(book_isbn):
    infolibro = db.execute("SELECT * FROM libros WHERE isbn = :book_isbn", {"book_isbn": book_isbn}).fetchall()
    isbn =  infolibro[0][0]
    title = infolibro[0][1]
    author =  infolibro[0][2]
    year = infolibro[0][3]
    resenas = db.execute("SELECT resena,usuario FROM resenas WHERE isbn = :isbn;", {"isbn": infolibro[0][0]}).fetchall()
    estrella="";
    if(request.method == 'POST'):
        resena = request.form.get('resena')
        if(request.form.get('estrella1')):
            estrella = request.form.get('estrella1')
        if(request.form.get('estrella2')):
            estrella = request.form.get('estrella2')
        if(request.form.get('estrella3')):
            estrella = request.form.get('estrella3')
        if(request.form.get('estrella4')):
            estrella = request.form.get('estrella4')
        if(request.form.get('estrella5')):
            estrella = request.form.get('estrella5')
        if(estrella and resena):
            db.execute("INSERT INTO resenas (resena, estrellas, usuario, isbn) VALUES (:resena, :estrellas, :usuario, :isbn)", {"resena": resena, "estrellas": estrella,"usuario": session['usuario'],"isbn": infolibro[0][0]})
            db.commit()
            resenas = db.execute("SELECT resena,usuario FROM resenas WHERE isbn = :isbn;", {"isbn": infolibro[0][0]}).fetchall()
            return render_template("libro.html",resenas=resenas,isbn=isbn,title=title,author=author,year=year)
        else:
            resenas = db.execute("SELECT resena,usuario FROM resenas WHERE isbn = :isbn;", {"isbn": infolibro[0][0]}).fetchall()
            return render_template("libro.html",error = "Favor de llenar todos los campos",resenas=resenas,isbn=isbn,title=title,author=author,year=year)
    else:
        return render_template("libro.html",resenas=resenas,isbn=isbn,title=title,author=author,year=year)

@app.route("/registrar", methods=["GET","POST"])
def registrar():
    if request.method == 'POST':
        usuario = request.form.get("usuario")
        correo = request.form.get("correo")
        contrasena = request.form.get("contrasena")
        if(usuario and contrasena): 
            try:
                db.execute("INSERT INTO usuarios (usuario, correo, contrasena) VALUES (:usuario, :correo, :contrasena)", {"usuario": usuario.strip(), "contrasena": contrasena.strip(),"correo": correo.strip()})               
                db.commit()
                return redirect('/')
            except:
                db.close()
                return render_template("registrar.html",error="Nombre de usuario ya registrado")
        else:           
            return render_template("registrar.html",error="No deje ningun campo vacio")
    else:
        return render_template("registrar.html")
@app.route("/logout", methods=["GET","POST"])
def logout():
    session.pop('usuario')
    return redirect('/')