import pytest
from Ahorcado import Ahorcado

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