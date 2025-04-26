from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(__file__)
FILES = {
    'events': os.path.join(BASE_DIR, 'events.json'),
    'businesses': os.path.join(BASE_DIR, 'businesses.json'),
    'opportunities': os.path.join(BASE_DIR, 'funding.json'),
}

# --------------------------
# Helper functions
# --------------------------
def load_data(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

# --------------------------
# Events API
# --------------------------
@app.route('/api/events', methods=['GET'])
def get_events():
    return jsonify(load_data(FILES['events']))

@app.route('/api/events', methods=['POST'])
def add_event():
    event = request.get_json()
    if not event:
        return jsonify({'error': 'Invalid data'}), 400
    events = load_data(FILES['events'])

    # Assign a simple auto-increment ID
    max_id = max((e.get('id', 0) for e in events), default=0)
    event['id'] = max_id + 1

    events.append(event)
    save_data(FILES['events'], events)
    return jsonify(event), 201

@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    events = load_data(FILES['events'])
    new_events = [event for event in events if event.get('id') != event_id]
    if len(events) == len(new_events):
        return jsonify({'error': 'Event not found'}), 404
    save_data(FILES['events'], new_events)
    return jsonify({'message': 'Event deleted successfully'}), 200

# --------------------------
# Businesses API
# --------------------------
@app.route('/api/businesses', methods=['GET'])
def get_businesses():
    return jsonify(load_data(FILES['businesses']))

@app.route('/api/businesses', methods=['POST'])
def add_business():
    business = request.get_json()
    if not business:
        return jsonify({'error': 'Invalid data'}), 400
    businesses = load_data(FILES['businesses'])

    # Assign a simple auto-increment ID
    max_id = max((b.get('id', 0) for b in businesses), default=0)
    business['id'] = max_id + 1

    businesses.append(business)
    save_data(FILES['businesses'], businesses)
    return jsonify(business), 201

@app.route('/api/businesses/<int:business_id>', methods=['DELETE'])
def delete_business(business_id):
    businesses = load_data(FILES['businesses'])
    new_businesses = [biz for biz in businesses if biz.get('id') != business_id]
    if len(businesses) == len(new_businesses):
        return jsonify({'error': 'Business not found'}), 404
    save_data(FILES['businesses'], new_businesses)
    return jsonify({'message': 'Business deleted successfully'}), 200

# --------------------------
# Funding Opportunities API
# --------------------------
@app.route('/api/opportunities', methods=['GET'])
def get_opportunities():
    return jsonify(load_data(FILES['opportunities']))

@app.route('/api/opportunities', methods=['POST'])
def add_opportunity():
    opportunity = request.get_json()
    if not opportunity:
        return jsonify({'error': 'Invalid data'}), 400
    opportunities = load_data(FILES['opportunities'])

    # Assign a simple auto-increment ID
    max_id = max((o.get('id', 0) for o in opportunities), default=0)
    opportunity['id'] = max_id + 1

    opportunities.append(opportunity)
    save_data(FILES['opportunities'], opportunities)
    return jsonify(opportunity), 201

@app.route('/api/opportunities/<int:opportunity_id>', methods=['DELETE'])
def delete_opportunity(opportunity_id):
    opportunities = load_data(FILES['opportunities'])
    new_opportunities = [opp for opp in opportunities if opp.get('id') != opportunity_id]
    if len(opportunities) == len(new_opportunities):
        return jsonify({'error': 'Opportunity not found'}), 404
    save_data(FILES['opportunities'], new_opportunities)
    return jsonify({'message': 'Opportunity deleted successfully'}), 200

# --------------------------
# Run Server
# --------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
