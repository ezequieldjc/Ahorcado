import random
import time
from os import system

class Ahorcado():
    palabras = []
    palabra = ''
    guia = ''
    lpalabra = 0
    puntaje = 0
    intentos = 3
    alias = ''
    dificultad = 0
    letrasing = ''

    def carga_universo (self):
        time.sleep(0.5)
        while self.dificultad != 1 and self.dificultad !=2 and self.dificultad !=3:
            try:
                self.dificultad=int(input("------------------Seleccione dificutad ( 1-Facil, 2-Medio, 3-Dificil ): "))
            except ValueError:
                print("------------------Eso no fue un numero, capo.")
        print('------------------Cargando Universo...')
        time.sleep(0.5)
        if self.dificultad == 1:
            self.palabras.append('ABECEDARIO')
            self.palabras.append('CAMPERA')
            self.palabras.append('CARPINCHO')
            self.palabras.append('COMPUTADORA')
            self.palabras.append('BARCO')
            self.palabras.append('TIMON')
        elif self.dificultad ==2:
            self.palabras.append('LIGAMENTO')
            self.palabras.append('PARALISIS')
            self.palabras.append('FISOTERAPEUTA')
            self.palabras.append('ELECTROENCEFALOGRAFISTA')
            self.palabras.append('TRIPLAY')
            self.palabras.append('ESPASTICIDAD')
        elif self.dificultad ==3:
            self.palabras.append('PARAPLEJIA')
            self.palabras.append('DISTROFIA')
            self.palabras.append('PLAGUICIDAS')
            self.palabras.append('PARALEPIPEDOS')
            self.palabras.append('ESTERNOCLEIDOMASTOIDEO')
            self.palabras.append('MAGNETOHIDRODINAMICA')
    
    def elegir_palabra(self):
        self.palabra = random.choice(self.palabras)
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

    def crea_guia(self, a):
        self.palabra = a
        self.lpalabra = self.largo_palabra(self, a) 
        for x in range(self.lpalabra):
            self.guia = self.guia + '_'  
        return self.guia
    
    def muestra_guia(self,a):
        y = 0
        muestra = ''
        y = self.largo_palabra(self, a)
        for x in range(y):
            muestra = muestra + a[x] + ' '
        return muestra

    def ingresa_letra(self, a):
        self.letrasing = self.letrasing + a
        if a in self.palabra:
            for i in range(self.lpalabra):
                if self.palabra[i] == a:
                    self.guia = self.guia[:i] + a + self.guia[i+1:]
        else: 
            self.intentos = self.intentos -1
        return self.guia

    def ingresa_alias(self, a):
        self.alias = a.upper()
        return self.alias

    def game(self):
        system("cls")
        print('------------------Bienvenido Al juego!')
        time.sleep(0.5)
        alias = input('------------------Imgrese su nombre: ')
        self.ingresa_alias(self, alias)
        opcion = 'SI'
        while opcion.upper() == 'SI' or opcion.upper() == 'S':
            system("cls")
            self.carga_universo(self)
            us = ''
            self.intentos = 6 - self.dificultad 
            self.elegir_palabra(self)
            self.crea_guia(self, self.palabra)
            print(f'------------------La palabra tiene {self.lpalabra} letras')
            us = self.muestra_guia(self, self.guia)
            print(f'------------------Su guia es: {us}')
            print(f'------------------Intentos Restantes: {self.intentos}')                
            time.sleep(0.5)
            b = 1
            while self.intentos > 0 and b==1:
                if self.dificultad !=3:
                    let = self.muestra_guia(self, self.letrasing)
                    print(f'------------------Letras ya ingresadas: {let}')
                ingreso = input("------------------Ingrese Letra o Arriesgue Palabra: ")
                system("cls")
                if len(ingreso) > 1:
                    if ingreso.upper() == self.palabra:
                        print("------------------Palabra Correcta!")
                        b = 2
                        self.dev_puntaje(self, 8)
                    else:
                        print(f"------------------La palabra {ingreso} es incorrecta")
                        b = 0
                else: 
                    self.ingresa_letra(self,ingreso.upper())
                    a = self.muestra_guia(self, self.guia) 
                    print(f'------------------La palabra tiene {self.lpalabra} letras')                    
                    print(f'------------------Su guia: {a}')
                    print(f'------------------Intentos Restantes: {self.intentos}')                    
                    if self.palabra == self.guia:
                        print("------------------Palabra Correcta!")
                        b = 2
                        self.dev_puntaje(self, self.intentos)    
            time.sleep(0.5)
            print("------------------Calculando Puntaje!..")
            time.sleep(0.5)
            print(f'------------------{self.alias} su Puntaje es de {self.puntaje}')
            time.sleep(0.5)
            if b ==2:
                opcion = input("------------------Continuar Jugando?(SI/NO): ")
            else: 
                opcion = 'N'
                print("------------------Perdiste!!")
                time.sleep(0.5)
                print(f'------------------La palabra era {self.palabra}')
                time.sleep(2)
            self.limpiar_variables_parcial(self)
        time.sleep(0.5)
        system("cls")
        print(f'------------------{self.alias} su Puntaje Final fue de {self.puntaje}')   
        time.sleep(0.5) 
        print('------------------¡Hasta la próxima!')
        self.limpiar_variables_total(self)
        