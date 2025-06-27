# Puerto 8000 o 8000/8181

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def show_ip():
    return f"La conexión se está realizando desde {request.remote_addr}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
