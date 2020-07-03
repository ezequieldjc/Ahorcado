from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, ForeignKey, Integer, String, Time, Date, DateTime
from sqlalchemy.sql import func
from datetime import timedelta, datetime
import random


db = SQLAlchemy()

class Jugadas(db.Model):
    __tablename__ = 'jugadas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    puntaje = db.Column(db.Integer)
    fecha = Column(DateTime(timezone=True), nullable=False, default=func.now()+ timedelta(hours=-3))

class Universo(db.Model):
    __tablename__ = 'universo'
    id = db.Column(db.Integer, primary_key=True)
    palabra = db.Column(db.String(30))
    dificultad = db.Column(db.Integer)


class Ahorcado(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True)
    palabra = db.Column(db.String(50))
    guia = db.Column(db.String(50))
    largopal = db.Column(db.Integer)
    puntaje = db.Column(db.Integer)
    intentos = db.Column(db.Integer)
    alias = db.Column(db.String(50))
    letrasing = db.Column(db.String(50))
    dificultad = db.Column(db.Integer)
    fecha = Column(DateTime(timezone=True), nullable=False, default=func.now())

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def carga_dificultad(self, a):
        self.dificultad = int(a)
        
    def carga_universo (self):
        print('------------------Cargando Universo...')
        qpalabras = Universo.query.filter(Universo.dificultad==self.dificultad).all()
        for x in qpalabras:
            self.palabras.append(x.palabra)
            print(f'------------------Palabra: {x.palabra} cargada.. ')  
        print('------------------Universo Cargado ')
    
    def elegir_palabra(self):
        print('------------------Cargando Palabra ')
        self.palabra = random.choice(self.palabras)
        print('------------------Palabra Cargada ')
        return self.palabra

    def cuenta_universo (self):  
        return len(self.palabras)

    def dev_puntaje (self, a):
        if a ==8:
            self.puntaje = self.puntaje + 15 * self.dificultad*2      
        if a ==1 or self.intentos==1:
            self.puntaje = self.puntaje + 2 * self.dificultad*2
        elif a ==2 or self.intentos==2:
            self.puntaje = self.puntaje + 4 * self.dificultad*2
        elif a ==3 or self.intentos==3:
            self.puntaje = self.puntaje + 6 * self.dificultad*2 
        elif a ==4 or self.intentos==4:
            self.puntaje = self.puntaje + 8 * self.dificultad*2 
        elif a ==5 or self.intentos==5:
            self.puntaje = self.puntaje + 10 * self.dificultad*2
        elif a ==0 or self.intentos==0:
            self.puntaje = self.puntaje * 1                              
        self.intentos = 0
        return self.puntaje 

    def largo_palabra(self,a):
        x = len(a)
        return x 
    
    def limpiar_variables_parcial(self):
        self.palabras = []
        self.palabra = ''
        self.guia = ''
        self.lpalabra = 0
        self.intentos = 5
        self.dificultad = 0
        self.letrasing = ''
    
    def limpiar_variables_total(self):
        self.palabras = []
        self.palabra = ''
        self.guia = ''
        self.lpalabra = 0
        self.puntaje = 0
        self.intentos = 5
        self.alias = ''
        self.dificultad = 0
        self.letrasing = ''

    def getIntentos(self):
        return self.intentos

    def crea_guia(self, ba):
        self.guia = ''
        self.palabra = ba
        self.lpalabra = self.largo_palabra(ba) 
        for x in range(self.lpalabra):
            self.guia = self.guia + '*'  
        return self.guia
    
    def muestra_guia(self,a):
        y = 0
        muestra = ''
        y = self.largo_palabra(a)
        for x in range(y):
            muestra = muestra + a[x] 
        return muestra

    def ingresa_letra(self, a):
        print(f'------------------Letra: {a}')
        self.letrasing = self.letrasing  + a + '-'
        if a in self.palabra:
            print('1')
            for i in range(self.lpalabra):
                print(i)
                if self.palabra[i] == a:
                    self.guia = self.guia[:i] + a + self.guia[i+1:]
        else: 
            self.intentos = self.intentos -1
        return self.guia

    def ingresa_alias(self, a):
        self.alias = a
        return self.alias
        