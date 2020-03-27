Proyecto Libreria TEC
El proyecto esta elaborado en FLASK y HTML, La base de datos que se utilizo fue
POSTGRESQL alojada en elephantSQL, la funcion principal es encontrar una diversa variedad de libros,
poder ver informacion sobre el, como el ISBN, el titulo del libro, el autor que lo escribio
y el año de su publicacion, también permite dejar reseñas sobres los libros que podran ver los demas usuarios.

import.py
Contiene el codigo para ingresar todos los registros del csv books.csv a la base de datos.

application.py
contiene todo el backend que hace funcionar a la pagina.

Requerimientos:
Flask
Flask-Session
psycopg2-binary
SQLAlchemy
