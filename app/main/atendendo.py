#!/usr/bin/env python3

from flask import Flask, render_template
import sqlite3
from sistema_suporte import Conexao

app = Flask(__name__)

@app.route('/atendendo')
def lista_chamados(name=None):
    c = Conexao()
    chamadas = c.lista_chamadas
    #movies = [dict(id=row[0], movie_name=row[1]) for row in cur.fetchall()]
    #return render_template('test.html', chats=chamadas)
    return render_template('atendendo.html', chats = suporte.query.all() )

"""
def connect_db():
    return sqlite3.connect('example.db')

def init_db():
    conn = connect_db()
    c = conn.cursor()
    try:
        c.execute('create table movies (id int, name text, category text)')
        c.execute('insert into movies (id, name, category) values (?, ?, ?)', (1, 'Alien', 'sci-fi'))
        c.execute('insert into movies (id, name, category) values (?, ?, ?)', (2, 'Aliens', 'sci-fi'))
        c.execute('insert into movies (id, name, category) values (?, ?, ?)', (3, 'Prometheus', 'sci-fi'))
    except sqlite3.OperationalError as e:
        assert 'table movies already exists' in str(e)
    conn.commit()
    conn.close()


def main():
    init_db()
"""
