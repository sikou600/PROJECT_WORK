import os
from flask import Flask, Response
from prometheus_client import start_http_server, Counter, generate_latest

app = Flask(__name__)

REQUESTS = Counter('http_requests_total', 'Total HTTP requests')

@app.route('/')
def hello():
    message = os.environ.get('landing_message', 'Hello!')
    REQUESTS.inc() 
    return message

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)