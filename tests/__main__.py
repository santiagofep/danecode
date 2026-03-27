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

    def test_empty_department_raises(self):
        with self.assertRaises(ValueError):
            get_data("", "Rionegro")

    def test_none_department_raises(self):
        with self.assertRaises(ValueError):
            get_data(None, "Rionegro")

    def test_empty_municipality_raises(self):
        with self.assertRaises(ValueError):
            get_data("Santander", "")


class TestCoordinadoraCenterOfPopulation(unittest.TestCase):

    def test_returns_expected_fields(self):
        place = coordinadora_center_of_population("MONTEZUMA (VALLE)")
        self.assertEqual(place["nombre_centro_poblado"], "MONTEZUMA")
        self.assertEqual(place["codigo_departamento"], "76")
        self.assertIn("codigo_municipio", place)
        self.assertIn("tipo", place)

    def test_empty_location_raises(self):
        with self.assertRaises(ValueError):
            coordinadora_center_of_population("")

    def test_invalid_format_raises(self):
        with self.assertRaises(ValueError):
            coordinadora_center_of_population("MONTEZUMA VALLE")

    def test_unknown_department_code_raises(self):
        with self.assertRaises(ValueError):
            coordinadora_center_of_population("MONTEZUMA (ZZZZZ)")


if __name__ == "__main__":
    unittest.main()
