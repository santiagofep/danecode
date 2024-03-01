import unittest

from danecode import coordinadora_center_of_population


class TestDanecodeMethods(unittest.TestCase):

    def test_coordinadora_center_of_population(self):
        place = coordinadora_center_of_population("MONTEZUMA (VALLE)")
        print(place)


if __name__ == "__main__":
    unittest.main()
