# flask_and_docker

---

¡Hola! 👋
Bienvenido/a a este proyecto donde exploramos cómo levantar apps Flask en una VM ubuntu, en diferentes puertos y también cómo “dockerizarlas” para llevarlas al siguiente nivel. Aquí te explico cómo puedes probar cada versión fácilmente, desde lo más básico hasta automatizaciones para que todo corra sin que tengas que preocuparte por nada.
Contenidos

1. Flask puro en puerto 8000

2. Flask con HTML/CSS en puerto 8181

3. Flask en Docker (puerto 8888)

4. Automatización y arranque automático

5. Validación y comandos útiles

---

## 1. Flask puro en puerto 8000

Esta app es la más sencilla, perfecta para testear tu entorno. Solo muestra la IP desde donde te conectas.
Cómo levantarla

Crea la carpeta y archivos:

    mkdir ~/flask8000
    cd ~/flask8000
    nano app.py

Copia y pega esto:

    from flask import Flask, request

    app = Flask(__name__)

    @app.route('/')
    def show_ip():
        return f"La conexión se está realizando desde {request.remote_addr}"

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)

Requisitos:
    
    nano requirements.txt
Dentro del archivo requirements.txt

    flask
    requests

Instala los requisitos:

    pip3 install -r requirements.txt

Ejecutar manualmente:

    python3 app.py

Visita http://localhost:8000


Imagen 2, Picture
---

## 2. Flask con HTML/CSS en puerto 8181

Aquí verás tu IP mostrada de manera más bonita usando HTML y CSS.
Cómo levantarla

Crea la estructura:

    mkdir -p ~/flask8181/templates ~/flask8181/static
    cd ~/flask8181

Archivos necesarios:

app.py

    from flask import Flask, render_template, request

    app = Flask(__name__)

    @app.route('/')
    def index():
        ip = request.remote_addr
        return render_template('index.html', ip=ip)

    if __name__ == '__main__':
    a    pp.run(host='0.0.0.0', port=8181)

requirements.txt

    flask
    requests

templates/index.html

    <!DOCTYPE html>
    <html>
    <head>
        <title>IP Viewer</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="content">
            <h1>Tu IP de conexión es:</h1>
            <p>{{ ip }}</p>
        </div>
    </body>
    </html>

static/style.css

    body {
        background-color: #eef;
        font-family: Arial, sans-serif;
        text-align: center;
        padding-top: 100px;
    }

Instala los requisitos:

    pip3 install -r requirements.txt

Ejecuta la app:

    python3 app.py

Abre http://localhost:8181

---

## 3. Flask en Docker (puerto 8888)

Aquí levantamos la app Flask usando Docker. ¡Ideal para ambientes productivos o cuando quieres olvidarte de las dependencias del sistema!
Cómo levantarla

Archivos básicos en una carpeta nueva:

    mkdir ~/flask8888
    cd ~/flask8888

app.py

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def index():
        return "¡Hola desde Docker en puerto 8888!"

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8888)

requirements.txt

    flask

Dockerfile

    FROM python:3.9
    WORKDIR /app
    COPY . .
    RUN pip install -r requirements.txt
    EXPOSE 8888
    CMD ["python", "app.py"]

run_docker.sh

    #!/bin/bash
    docker build -t flask8888 .
    docker run -d -p 8888:8888 --name flask_container flask8888

Hazlo ejecutable:

    chmod +x run_docker.sh

Construye y ejecuta:

    ./run_docker.sh

Si prefieres el comando directo:

    docker build -t flask8888 .
    docker run -d -p 8888:8888 --name flask_container flask8888

Accede en tu navegador http://localhost:8888

## 4. Automatización y arranque automático

Para que Flask (puerto 8000) se levante al iniciar sesión:
Agrega esto al final de ~/.bashrc:

    bash ~/flask8000/start_flask.sh &

Y el archivo start_flask.sh:

    #!/bin/bash
    cd ~/flask8000
    python3 app.py

Recuerda:

    chmod +x ~/flask8000/start_flask.sh

Para Docker:
Si quieres que el contenedor se reinicie siempre que la máquina se apague/prenda, usa:

    docker run -d -p 8888:8888 --restart always --name flask_container flask8888

---

## 5. Validación y comandos útiles

¿Está Flask o Docker corriendo?

    docker ps

Detener el contenedor:

    docker stop flask_container
    docker rm flask_container

Ver logs de Flask en Docker:

    docker logs flask_container

---

## 👥 Integrantes del equipo

| Nombre        | GitHub Usuario        |
|---------------|------------------------|
|Leandro Rain|   [@leoRV14].
|Francheska Tapia| [@FrancheskaTapia].
