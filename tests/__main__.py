import unittest

from danecode import get_data, coordinadora_center_of_population


class TestGetData(unittest.TestCase):

    def test_exact_match(self):
        result = get_data("Santander", "Rionegro")
        self.assertEqual(result["department"], "Santander")
        self.assertEqual(result["department_code"], "68")
        self.assertEqual(result["municipality"], "Rionegro")
        self.assertEqual(result["municipality_code"], "68615")

    def test_fuzzy_match(self):
        result = get_data("Santnder", "Riongro")
        self.assertEqual(result["department"], "Santander")
        self.assertEqual(result["municipality"], "Rionegro")

    def test_bogota(self):
        result = get_data("Bogotá D.C.", "Bogotá D.C.")
        self.assertEqual(result["department_code"], "11")


class TestCoordinadoraCenterOfPopulation(unittest.TestCase):

    def test_returns_expected_fields(self):
        place = coordinadora_center_of_population("MONTEZUMA (VALLE)")
        self.assertEqual(place["nombre_centro_poblado"], "MONTEZUMA")
        self.assertEqual(place["codigo_departamento"], "76")
        self.assertIn("codigo_municipio", place)
        self.assertIn("tipo", place)


if __name__ == "__main__":
    unittest.main()
