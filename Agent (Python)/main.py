from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from my_agent import agent
import threading
from datetime import datetime
import socket_service
import os
import secrets
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)

CORS(app, origins="*")

socketio = SocketIO(app, cors_allowed_origins="*")

socket_service.set_socketio_instance(socketio)

# Global variable to store the current socket session
current_socket_session = None

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Area51 Project IBM Agent!"


@socketio.on('connect')
def handle_connect():
    global current_socket_session
    current_socket_session = request.sid
    socket_service.set_current_session(request.sid)
    emit('status', {'message': 'Connected to agent server'})
    socket_service.emit_log('🔌 Client connected to agent server', 'success')


@socketio.on('disconnect')
def handle_disconnect():
    global current_socket_session
    current_socket_session = None
    socket_service.set_current_session(None)
    print(f"Client disconnected: {request.sid}")


def emit_log(message, log_type='info'):
    """Helper function to emit logs to connected clients"""
    socket_service.emit_log(message, log_type)


@app.route('/fix', methods=['POST'])
def fix():
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response
    
    data = request.get_json()
    project_path = data.get('project_path', '')
    session_id = data.get('session_id', '')
    user_instructions = data.get('user_instructions', '')


    def run_agent_async():
        try:
            emit_log(f"🚀 Starting agent session: {session_id}", 'info')
            emit_log(f"📁 Project path: {project_path}", 'info')
            if user_instructions:
                emit_log(f"📝 User instructions: {user_instructions}", 'info')
            
            # Set the current session for this thread
            socket_service.set_current_session(current_socket_session)
            
            log = agent(project_path, session_id, user_instructions)
            
            emit_log("✅ Agent session completed successfully", 'success')
            socketio.emit('agent_complete', {
                'log': log,
                'session_id': session_id
            }, room=current_socket_session)
        except Exception as e:
            emit_log(f"❌ Error in agent execution: {str(e)}", 'error')
            socketio.emit('agent_error', {
                'error': str(e),
                'session_id': session_id
            }, room=current_socket_session)

    # Run agent in background thread to avoid blocking
    thread = threading.Thread(target=run_agent_async, name=f"AgentThread-{session_id}")
    thread.daemon = False  # Don't make it a daemon thread
    thread.start()

    response = jsonify({
        'message': 'Agent started',
        'session_id': session_id
    })
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)