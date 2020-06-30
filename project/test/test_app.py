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
def  test_largoPalabra():
    a = Ahorcado
    actual = a.largo_palabra(a, 'Gato')
    expected = 4
    assert expected == actual

#Pruebo guia 
def test_letra_existe():
    a = Ahorcado
    a.limpiar_variables(a)
    a.crea_guia(a,'CHAPA')
    actual = a.ingresa_letra(a,'A')
    expected = '__A_A'
    assert expected == actual