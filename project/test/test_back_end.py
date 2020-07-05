import pytest
from project.ahorcado import Ahorcado

def test_prueba():
    a = Ahorcado
    dif = 2
    a.carga_dificultad(a,dif)
    actual = a.devuelve_dificultad(a)
    expected = dif
    assert expected == actual

#Pruebo largo de una palabra
def  test_largo_palabra():
    a = Ahorcado
    actual = a.largo_palabra(a, 'Gato')
    expected = 4
    assert expected == actual

#Pruebo guia 
def test_letra_existe():
    a = Ahorcado
    a.limpiar_variables_total(a)
    a.crea_guia(a,'CHAPA')
    actual = a.ingresa_letra_obj(a,'A')
    expected = '__A_A'
    assert expected == actual

#def test_puntaje_acierto():
#    a = Ahorcado
#    a.limpiar_variables_total(a)
#    actual = a.dev_puntaje(a,8)
#    expected = 200
#    assert expected == actual

#def test_caracteres_a_insertar():
#    a = Ahorcado
#    a.limpiar_variables_total(a)
#    actual = a.crea_guia(a,'CHAPA')
#    expected = '_____'
#    assert expected == actual

#def test_intentos_restantes():
#    a = Ahorcado
#    a.limpiar_variables_total(a)
#    a.crea_guia(a,'CHAPA')
#    actual = a.get_intentos(a)
#    a.ingresa_letra (a, 'B')
#    expected = a.get_intentos(a) + 1
#    assert actual == expected

def test_ingresa_alias():
    a = Ahorcado
    actual =  a.ingresa_alias(a,'aLiAs')    
    expected = 'ALIAS'
    assert actual == expected

#def test_cambio_puntaje():
#    a = Ahorcado
#    a.limpiar_variables_total(a)
#    a.carga_dificultad(a, 2)
#    actual = a.dev_puntaje (a, 3)
#    expected = 60
#    assert actual == expected