## Amy Finnegan - Homework 1
## HW1test.py
## This file tests HW1.py


import unittest
import HW1

class TestHW1Code(unittest.TestCase):

	def setUP (self):
		return 

		## shout tests
		
		## No bugs
		
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
		
		##  Bugs: Does not capitalize in sentence case.  Puts a " " after the "."  Fixed.

		
	def test_reversewords(self):
		self.assertEqual(HW1.reversewords('Do it right this time.'), "Time this right it do.")
	
		## reversewordletters test
		
		## Bugs: Drops last word if there is not punctuation.  Fixed.
		
	def test_reversewordletters(self):
		self.assertEqual(HW1.reversewordletters('Do it right this time?'), "oD ti thgir siht emit?")
		
	def test_reversewordletters(self):
		self.assertEqual(HW1.reversewordletters('Reverse absent punctuation'),
			"esreveR tnesba noitautcnup")

	
		## Pig Latin test
		
		## Not working.  Fixed!
		
	def test_piglatin_qu(self):
		self.assertEqual(HW1.piglatin('question'), "estion-quay")
		
	def test_piglatin_vowels(self):
		self.assertEqual(HW1.piglatin('angina'), "angina-ay")
		
	def test_piglatin_cons(self):
		self.assertEqual(HW1.piglatin('dinosaur'), "inosaur-day")

		
if __name__=='__main__':
	unittest.main()
	
