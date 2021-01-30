from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from sistema_suporte import Conexao
import re


@socketio.on('joined', namespace='/chat')
def joined(message):
    #import pudb;pu.db
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    # nao funciona abaixo
    #if len(room)>14:
    #    room = re.sub('[^0-9]', '', room)
    join_room(room)
    #c = Conexao()
    #c.grava_conversa(room, session.get('name'), '2020.05.08 10:00:00', 'Suporte', 'Suporte')
    emit('status', {'msg': session.get('name') + ' acessou o suporte.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    #import pudb;pu.db
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    c = Conexao()
    sessao = session.get('csrf_token')
    c.grava_conversa(room, session.get('name'), '2020.05.08 10:00:00', message['assunto'], message['msg'])
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' fechou o suporte.'}, room=room)

