from flask import Flask
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL no esta definida en las variables de entorno")

#set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route('/')
def index():
    return '<h1>Hola Knauth, <span style="background-color: red">:p</span></h1>'

@app.route('/index/<string:nombre>')
def home(nombre):
    return f'<h1>Hola</h1><h3>Bienvenido {nombre}</h3>'

if __name__ == '__main__':
    app.run()