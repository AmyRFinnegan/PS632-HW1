## HW1test.py

"""
Tests
	assertTrue
	assertFalse
	assertEqual
	assertNotEqual
For floats (2.2, 3.1, etc)
	assertAlmostEqual
	assertNotAlmostEqual
"""

import unittest
import HW1

class TestHW1Code(unittest.TestCase):

	def setUP (self):
		return 

		## shout tests
		
	def test_shout_word(self):
		self.assertEqual(HW1.shout('word'), "WORD!")
		
	def test_shout_word2(self):
		self.assertNotEqual(HW1.shout('word'), "word")
		
		## reverse letter tests
	
	def test_reverse(self):
		self.assertEqual(HW1.reverse('straw'), 'warts')
	straw = 'straw'
	warts = 'warts'
	print "If I reverse %s, I get %s. o_O"  %(straw, warts) 
	
	def test_reverse_2(self):
		txt = HW1.reverse('spoons')
		rtxt = 'spoons'
		print "If I reverse %s, I get %s. :)" % (rtxt, txt)
		tmp = 1
		for i in range(len(txt)) :
			self.assertEqual(txt[i], rtxt[-tmp])
			tmp += 1
		
			
		## reversewords test
		
	def test_reversewords(self):
		self.assertEqual(HW1.reversewords('Do it right this time.'), "Time this right it do.")
	
		## reversewordletters test
		
	def test_reversewordletters(self):
		self.assertEqual(HW1.reversewordletters('Do it right this time?'), "oD ti thgir siht emit?")

	
		## Pig Latin test

		
if __name__=='__main__':
	unittest.main()
	
