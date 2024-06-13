from gestion_sensores import *
from numpy import mean, median, std
import pytest

def test_unica_instancia_singleton():
    gestor_a = Gestor.obtener_instancia()
    gestor_b = Gestor.obtener_instancia()
    assert gestor_a == gestor_b

def test_successor():
    with pytest.raises(Exception):
        calculo_datos = Estadisticos('ejemplo')

def test_establecer_estrategia():
    with pytest.raises(Exception):
        datos_ejemplo = [4, 9, -2, 7, 1, -6, 19, -3, 14, -9]
        contexto = ContextoCalculoEstadisticos(datos_ejemplo)
        contexto.establecerEstrategia('ejemplo')

def test_calculo_estadisticos1():
    datos_ejemplo = [4, 9, -2, 7, 1, -6, 19, -3, 14, -9]
    media_calculo = Media('media')
    contexto = ContextoCalculoEstadisticos(datos_ejemplo)
    contexto.establecerEstrategia(media_calculo)
    media_resultado, de_resultado = contexto.calculoEstadisticos()
    media_esperada = round(mean(datos_ejemplo), 2)
    de_esperado = round(std(datos_ejemplo), 2)
    assert media_resultado == media_esperada and de_resultado == de_esperado

def test_calculo_estadisticos2():
    datos_ejemplo = [4, 9, -2, 7, 1, -6, 19, -3, 14, -9]
    mediana_calculo = Mediana('mediana')
    contexto = ContextoCalculoEstadisticos(datos_ejemplo)
    contexto.establecerEstrategia(mediana_calculo)
    mediana_resultado = contexto.calculoEstadisticos()
    mediana_esperada = median(datos_ejemplo)
    assert mediana_resultado == mediana_esperada

def test_calculo_estadisticos3():
    datos_ejemplo = [4, 9, -2, 7, 1, -6, 19, -3, 14, -9]
    maximos_calculo = Maximo('maximos')
    contexto = ContextoCalculoEstadisticos(datos_ejemplo)
    contexto.establecerEstrategia(maximos_calculo)
    max_resultado, min_resultado = contexto.calculoEstadisticos()
    max_esperado = max(datos_ejemplo)
    min_esperado = min(datos_ejemplo)
    assert max_resultado == max_esperado and min_resultado == min_esperado
