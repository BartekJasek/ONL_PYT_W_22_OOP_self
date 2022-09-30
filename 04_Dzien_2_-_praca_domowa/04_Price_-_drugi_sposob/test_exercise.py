import unittest

import exercise


class Price23VatTestCase(unittest.TestCase):
    def test_creating_instance(self):
        p = exercise.Price23Vat(123)

    def test_reading(self):
        p = exercise.Price23Vat(123)
        self.assertAlmostEqual(p.netto, 100)
        self.assertEqual(p.brutto, 123)
        self.assertAlmostEqual(p.tax, 23)

    def test_setting_netto(self):
        p = exercise.Price23Vat(123)
        p.netto = 200
        self.assertEqual(p.netto, 200)
        self.assertAlmostEqual(p.brutto, 246)
        self.assertAlmostEqual(p.tax, 46)

    def test_setting_brutto(self):
        p = exercise.Price23Vat(123)
        p.brutto = 246
        self.assertAlmostEqual(p.netto, 200)
        self.assertEqual(p.brutto, 246)
        self.assertAlmostEqual(p.tax, 46)

    def test_setting_tax(self):
        p = exercise.Price23Vat(123)
        p.tax = 46
        self.assertAlmostEqual(p.netto, 200)
        self.assertAlmostEqual(p.brutto, 246)
        self.assertEqual(p.tax, 46)
