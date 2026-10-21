from calculadora import sumar


def test_cadena_vacia_devuelve_cero():
    assert sumar("") == 0


def test_sumar_un_numero():
    assert sumar("5") == 5
