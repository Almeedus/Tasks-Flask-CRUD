from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

#criando rota = comunicação com cliente(usuario)
@app.route("/")
def hello_world():
    return f'Hello World'

@app.route("/about")
def sobre():
    return f'Pagina sobre programação.'

if __name__ == "__main__":
    app.run(debug=True)