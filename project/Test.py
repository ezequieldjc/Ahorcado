import unittest

class TestSprint1(unittest.TestCase):
 #Pruebo la cantidad de palabras en el universo 
  def test_cant_universo(self):
    a = Ahorcado
    a.limpiar_variables(a)
    a.carga_universo(a)
    b = a.cuenta_universo(a)
    self.assertEqual(6,b)

 #Pruebo largo de una palabra
  def test_palabra(self):
    a = Ahorcado
    a.limpiar_variables(a)
    b = a.largo_palabra(a, 'Gato')
    self.assertEqual(b, 4)

 #Pruebo acierto de arriegar palabra
  def test_puntaje_acierto(self):
    a = Ahorcado
    a.limpiar_variables(a)
    b = a.dev_puntaje(a, 8)
    self.assertEqual(b, 200)

#Pruebo catidad de caracteres a insertar
  def test_caracteres_a_insertar(self):
    a = Ahorcado
    a.limpiar_variables(a)
    b = a.crea_guia(a,'Chapa')
    self.assertEqual(b,'_____')

#Pruebo cantidad de intentos restastes
  def test_intentos_restantes(self):
    a = Ahorcado
    a.limpiar_variables(a)
    a.crea_guia(a,'CHAPA')
    a.ingresa_letra (a, 'B')
    b = a.getIntentos (a)
    self.assertEqual(b,2)
    
#Pruebo letra existente
  def test_letra_existe(self):
    a = Ahorcado
    a.limpiar_variables(a)
    a.crea_guia(a,'CHAPA')
    b = a.ingresa_letra (a, 'A')
    self.assertEqual(b,'__A_A')

#Pruebo cambios en el puntaje
  def test_cambio_puntaje(self):
    a = Ahorcado
    a.limpiar_variables(a)    
    #No deberiamos setear la variable de dificultad ? 
    #Si la rta es si, se debe agregar esta linea
    # a.dificultad = 2
    b = a.dev_puntaje (a, 3)
    self.assertEqual(b,60)

#Pruebo el ingresa alias
  def test_ingresa_alias(self):
    a = Ahorcado
    alias = a.ingresa_alias(a,'aLiAs')    
    self.assertEqual(alias,'ALIAS')

#Pruebo cambios en el puntaje
  def test_cambio_puntaje(self):
    a = Ahorcado
    a.limpiar_variables(a)    
    #No deberiamos setear la variable de dificultad ? 
    #Si la rta es si, se debe agregar esta linea
    # a.dificultad = 2
    b = a.dev_puntaje (a, 3)
    self.assertEqual(b,60)
