from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
from datetime import datetime
import os

# Create Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# Initialize Socket.IO
socketio = SocketIO(app, cors_allowed_origins="*")

# For PythonAnywhere deployment
application = app

# Store buzzer state
buzzer_state = {
    'is_active': True,
    'buzzer_order': [],
    'table_states': {str(i): {'points': 0, 'buzzed': False} for i in range(1, 12)}
}

def get_rankings():
    rankings = [{'table': table, 'points': state['points']} 
                for table, state in buzzer_state['table_states'].items()]
    return sorted(rankings, key=lambda x: x['points'], reverse=True)

@app.route('/')
def index():
    # Get current rankings when page loads
    rankings = get_rankings()
    return render_template('index.html', rankings=rankings)

@app.route('/host')
def host():
    return render_template('host.html')

@app.route('/connect')
def connect():
    return render_template('connect.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@socketio.on('connect')
def handle_connect():
    # Send current rankings to newly connected client
    emit('rankings_update', {'rankings': get_rankings()})

@socketio.on('buzz')
def handle_buzz(data):
    table_id = str(data['table_id'])
    if buzzer_state['is_active'] and not buzzer_state['table_states'][table_id]['buzzed']:
        buzzer_state['table_states'][table_id]['buzzed'] = True
        buzzer_state['buzzer_order'].append(table_id)
        order = len(buzzer_state['buzzer_order'])
        
        # Emit buzz event without awarding points
        emit('buzz_received', {
            'table_id': table_id,
            'order': order,
            'rankings': get_rankings()
        }, broadcast=True)

@socketio.on('award_points')
def award_points(data):
    table_id = str(data['table_id'])
    points = data['points']  # Host will specify how many points to award
    
    # Award the points
    buzzer_state['table_states'][table_id]['points'] += points
    
    # Emit updated rankings
    emit('points_updated', {
        'table_id': table_id,
        'points_awarded': points,
        'rankings': get_rankings()
    }, broadcast=True)

@socketio.on('reset_buzzers')
def reset_buzzers():
    buzzer_state['is_active'] = True
    buzzer_state['buzzer_order'] = []
    for table in buzzer_state['table_states']:
        buzzer_state['table_states'][table]['buzzed'] = False
    emit('buzzers_reset', broadcast=True)

@socketio.on('reset_points')
def reset_points():
    for table in buzzer_state['table_states']:
        buzzer_state['table_states'][table]['points'] = 0
    emit('points_reset', broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
