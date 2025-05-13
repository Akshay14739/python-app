from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/details')

def hello():
    return jsonify({
        'name': 'Flask App',
        'Time': datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    })

@app.route('/api/v1/healthz')

def route():
    return jsonify({
        'status': 'Up',
        'Message': 'I will Rock Backstage', 
        'Hostname': socket.gethostname(),
        'Time': datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")
# '/api/v1/details'
# '/api/v1/healthz'