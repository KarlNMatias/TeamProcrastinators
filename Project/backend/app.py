from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

events = []

@app.route('/api/events', methods=['GET', 'POST'])
def handle_events():
    if request.method == 'POST':
        data = request.json
        data['id'] = len(events) + 1
        events.append(data)
        return jsonify(data), 201
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
