#!/usr/bin/env python

from KataRomanNumerals import convert_arabics
import unittest


class TestRomans(unittest.TestCase):

    def test_other_numbers(self):
        self.assertEqual(convert_arabics(999), "CMXCIX")
        self.assertEqual(convert_arabics(145), "CXLV")
        self.assertEqual(convert_arabics(100), "C")

    def test_table_numbers(self):
        self.assertEqual(convert_arabics(1000), "M")
        self.assertEqual(convert_arabics(500), "D")
        self.assertEqual(convert_arabics(100), "C")
        self.assertEqual(convert_arabics(50), "L")
        self.assertEqual(convert_arabics(10), "X")
        self.assertEqual(convert_arabics(5), "V")
        self.assertEqual(convert_arabics(1), "I")

    def test_less_them_fifty(self):
        self.assertEqual(convert_arabics(41), "XLI")
        self.assertEqual(convert_arabics(42), "XLII")
        self.assertEqual(convert_arabics(43), "XLIII")
        self.assertEqual(convert_arabics(44), "XLIV")
        self.assertEqual(convert_arabics(45), "XLV")
        self.assertEqual(convert_arabics(46), "XLVI")
        self.assertEqual(convert_arabics(47), "XLVII")
        self.assertEqual(convert_arabics(48), "XLVIII")
        self.assertEqual(convert_arabics(49), "XLIX")

    def test_less_them_thirty(self):
        self.assertEqual(convert_arabics(20), "XX")
        self.assertEqual(convert_arabics(21), "XXI")
        self.assertEqual(convert_arabics(22), "XXII")
        self.assertEqual(convert_arabics(23), "XXIII")
        self.assertEqual(convert_arabics(24), "XXIV")
        self.assertEqual(convert_arabics(25), "XXV")
        self.assertEqual(convert_arabics(26), "XXVI")
        self.assertEqual(convert_arabics(27), "XXVII")
        self.assertEqual(convert_arabics(28), "XXVIII")
        self.assertEqual(convert_arabics(29), "XXIX")

    def test_less_them_twenty(self):
        self.assertEqual(convert_arabics(10), "X")
        self.assertEqual(convert_arabics(11), "XI")
        self.assertEqual(convert_arabics(12), "XII")
        self.assertEqual(convert_arabics(13), "XIII")
        self.assertEqual(convert_arabics(14), "XIV")
        self.assertEqual(convert_arabics(15), "XV")
        self.assertEqual(convert_arabics(16), "XVI")
        self.assertEqual(convert_arabics(17), "XVII")
        self.assertEqual(convert_arabics(18), "XVIII")
        self.assertEqual(convert_arabics(19), "XIX")

    def test_less_them_five(self):
        self.assertEqual(convert_arabics(1), "I")
        self.assertEqual(convert_arabics(2), "II")
        self.assertEqual(convert_arabics(3), "III")
        self.assertEqual(convert_arabics(4), "IV")

    def test_less_them_ten(self):
        self.assertEqual(convert_arabics(5), "V")
        self.assertEqual(convert_arabics(6), "VI")
        self.assertEqual(convert_arabics(7), "VII")
        self.assertEqual(convert_arabics(8), "VIII")
        self.assertEqual(convert_arabics(9), "IX")
