import os
import sys
from datetime import datetime, date, timedelta
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

 
Base = declarative_base()
 
class Suporte(Base):
    __tablename__ = 'suporte'
    id = Column(Integer, primary_key=True,  autoincrement=True)
    cliente = Column(String(20), nullable=False)
    contato = Column(String(60), nullable=False)
    data_suporte = Column(DateTime(timezone=True), default=func.now())
    suporte = Column(String(60), nullable=False)
    descricao = Column(String(120), nullable=False)
    situacao = Column(String(20), default='nova')
    atendente = Column(String(20))
    #link = Column(String(60))
    
 
class Conexao(object):
    """
    DB_ENGINE = {
        SQLITE: 'sqlite:////home/publico/desenv/python/suporte.db'
    }

    db_engine = None
    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in DB_ENGINE")    
    """

    def inicia_bd(self):
        engine = create_engine('sqlite:////home/publico/desenv/python/suporte.db')
        #Base.metadata.drop_all(engine) # usado pra excluir BD e criar novamente.
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
        
    def grava_conversa(self, cliente, contato, data_suporte, suporte, descricao):
        #link = 'http://127.0.0.1:8000/?cnpj=%s&name=' \
        #        %(cliente)
        conversa = Suporte(cliente=cliente, contato=contato, 
            suporte=suporte, descricao=descricao)
        ses = self.inicia_bd()
        ses.add(conversa)
        ses.commit()
        
    def busca_conversa(self, cliente, contato):
        ses = self.inicia_bd()
        #import pudb;pu.db
        conversa = (
            ses.query(Suporte)
            .filter(Suporte.cliente == cliente, 
                Suporte.contato == contato
            )
        )
        for cnv in conversa:
            return conversa
        return 'NADA'

    def lista_chamada(self):
        ses = self.inicia_bd()
        #import pudb;pu.db
        data_atual = date.today()
        hoje = '%s-%s-%s 03:00:00' %(str(data_atual.year),
             str(data_atual.month).zfill(2),
            str(data_atual.day).zfill(2))
        conversa = (
            ses.query(Suporte)
            .filter(Suporte.data_suporte > hoje
            )
        )
        #conversa = ses.query(Suporte).all()

        for cnv in conversa:
            return conversa
        return 'NADA'
