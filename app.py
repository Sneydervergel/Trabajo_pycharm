from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():

    #app.logger.debug('iniciando el debug')
    #app.logger.info('iniciando info')
    #app.logger.warning('iniciando a nivel warning')
    #app.logger.error('iniciando a nivel de error')
    app.logger.info(f'solicitud en la ruta {request.path}')
    return "<p>hello,world! desde Pycharm</p>"
@app.route("/saludar/<nombre>")
def saludar (nombre):
    app.logger.info(f'solicitud en la ruta{request.path}')
    return f"hola{nombre}"

@app.route("/edad/<int:edad>")
def edad(edad):
    app-logger.info(f'solicitud en la ruta{request.path}')
    return f"tu edad es {edad}"
#REST
@app.get("/api/user/<user>")
def user(user):
    valores = {'user': user}
    return valores