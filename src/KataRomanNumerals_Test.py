#!/usr/bin/env python

from KataRomanNumerals import convert_to_arabic
import unittest


class TestRomans(unittest.TestCase):

    def test_other_numbers(self):
        self.assertEqual(convert_to_arabic(999), "CMXCIX")
        self.assertEqual(convert_to_arabic(145), "CXLV")
        self.assertEqual(convert_to_arabic(100), "C")
        self.assertEqual(convert_to_arabic(1904), "MCMIV")
        self.assertEqual(convert_to_arabic(2008), "MMVIII")
        self.assertEqual(convert_to_arabic(47), "XLVII")

    def test_table_numbers(self):
        self.assertEqual(convert_to_arabic(1000), "M")
        self.assertEqual(convert_to_arabic(500), "D")
        self.assertEqual(convert_to_arabic(100), "C")
        self.assertEqual(convert_to_arabic(50), "L")
        self.assertEqual(convert_to_arabic(10), "X")
        self.assertEqual(convert_to_arabic(5), "V")
        self.assertEqual(convert_to_arabic(1), "I")

    def test_less_them_fifty(self):
        self.assertEqual(convert_to_arabic(41), "XLI")
        self.assertEqual(convert_to_arabic(42), "XLII")
        self.assertEqual(convert_to_arabic(43), "XLIII")
        self.assertEqual(convert_to_arabic(44), "XLIV")
        self.assertEqual(convert_to_arabic(45), "XLV")
        self.assertEqual(convert_to_arabic(46), "XLVI")
        self.assertEqual(convert_to_arabic(47), "XLVII")
        self.assertEqual(convert_to_arabic(48), "XLVIII")
        self.assertEqual(convert_to_arabic(49), "XLIX")

    def test_less_them_thirty(self):
        self.assertEqual(convert_to_arabic(20), "XX")
        self.assertEqual(convert_to_arabic(21), "XXI")
        self.assertEqual(convert_to_arabic(22), "XXII")
        self.assertEqual(convert_to_arabic(23), "XXIII")
        self.assertEqual(convert_to_arabic(24), "XXIV")
        self.assertEqual(convert_to_arabic(25), "XXV")
        self.assertEqual(convert_to_arabic(26), "XXVI")
        self.assertEqual(convert_to_arabic(27), "XXVII")
        self.assertEqual(convert_to_arabic(28), "XXVIII")
        self.assertEqual(convert_to_arabic(29), "XXIX")

    def test_less_them_twenty(self):
        self.assertEqual(convert_to_arabic(10), "X")
        self.assertEqual(convert_to_arabic(11), "XI")
        self.assertEqual(convert_to_arabic(12), "XII")
        self.assertEqual(convert_to_arabic(13), "XIII")
        self.assertEqual(convert_to_arabic(14), "XIV")
        self.assertEqual(convert_to_arabic(15), "XV")
        self.assertEqual(convert_to_arabic(16), "XVI")
        self.assertEqual(convert_to_arabic(17), "XVII")
        self.assertEqual(convert_to_arabic(18), "XVIII")
        self.assertEqual(convert_to_arabic(19), "XIX")

    def test_less_them_five(self):
        self.assertEqual(convert_to_arabic(1), "I")
        self.assertEqual(convert_to_arabic(2), "II")
        self.assertEqual(convert_to_arabic(3), "III")
        self.assertEqual(convert_to_arabic(4), "IV")

    def test_less_them_ten(self):
        self.assertEqual(convert_to_arabic(5), "V")
        self.assertEqual(convert_to_arabic(6), "VI")
        self.assertEqual(convert_to_arabic(7), "VII")
        self.assertEqual(convert_to_arabic(8), "VIII")
        self.assertEqual(convert_to_arabic(9), "IX")
