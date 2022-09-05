import unittest
from urllib import response

from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-DO List</title>', html)
        self.assertTrue(html.endswith('</html>'))

class TestStringMethods(unittest.TestCase):
	# test function to test equality of two value
	def test_negative(self):
		firstValue = "geeks"
		secondValue = "gfg"
		# error message in case if test case got failed
		message = "First value and second value are not equal !"
		# assertEqual() to check equality of first & second value
		self.assertEqual(firstValue, secondValue, message)

if __name__ == '__main__':
	unittest.main()

# #  Create your tests here.
# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1+1, 2)