from flask import Flask,render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def inicio():
    return render_template('principal.html')

if __name__=='__main__':
    app.run(debug=True)
