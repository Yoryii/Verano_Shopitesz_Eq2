from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/login')
def login():
    return render_template('Usuarios/login.html')

@app.route('/usuarios/new')
def registrarUsuario():
    return render_template('Usuarios/registrar.html')

if __name__=='__main__':
    app.run(debug=True)