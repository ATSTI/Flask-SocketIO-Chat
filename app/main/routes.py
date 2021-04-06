from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm
from sistema_suporte import Conexao
from sistema_suporte import Suporte


@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    #import pudb;pu.db
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        nome = request.args.get("name")
        sala = request.args.get("cnpj")
        #form.name.data = session.get('name', '')
        #form.room.data = session.get('room', '')
        form.name.data = nome
        form.room.data = sala
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    #import pudb;pu.db
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)

@main.route('/atendendo')
def atendendo():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    #import pudb;pu.db
    #if name == '' or room == '':
    #    return redirect(url_for('.index'))
    c = Conexao()
    chats = c.lista_chamada()
    #for x in chats:
    #    z = x.descricao
    #    y = x.suporte
    #    w = x.contato
    #movies = [dict(id=row[0], movie_name=row[1]) for row in cur.fetchall()]
    #return render_template('atendendo.html', chats=chamadas)
    #return render_template('atendendo.html', name=name, room=room)
    return render_template('atendendo.html', chats=chats)
