import unittest
from main import buscar_datos
from database import database

class TestBuscarDatos(unittest.TestCase):

    def test_busqueda_exitosa(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", database=database)
        self.assertEqual(resultado, 1)

    def test_nombres_no_ordenados(self):
        resultado = buscar_datos('Diego','Pablo', 'Picasso','Ruiz', database=database)
        self.assertEqual(resultado, 2)

    def test_sin_existencia(self):
        resultado = buscar_datos("Juan", "Carlos", "García", database=database)
        self.assertIsNone(resultado)

    def test_busqueda_con_apellido_faltante(self):
        resultado = buscar_datos("Elias", "Marcos", database=database)
        self.assertIsNone(resultado)

    def test_busqueda_con_nombre_extra(self):
        resultado = buscar_datos("Elias", "Marcos", "Luciano", "Juan", database=database)
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()
