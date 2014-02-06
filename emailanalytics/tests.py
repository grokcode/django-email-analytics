from django.test import TestCase
from collections import OrderedDict
from bs4 import BeautifulSoup
from emailanalytics.text_processing import replace_urls_html, replace_urls_text, append_tracking


class ReplacementTestCase(TestCase):


    def test_tracking_append(self):

        params = OrderedDict()
        params['utm_source'] = 'This is the email subject'
        params['utm_medium'] = 'email'

        url = 'http://example.com'
        a_url = 'http://example.com?utm_source=This+is+the+email+subject&utm_medium=email'
        self.assertEqual(append_tracking(url, params), a_url) 

        url = 'http://example.com?test=ssss&test2=tttt'
        a_url = 'http://example.com?test=ssss&test2=tttt&utm_source=This+is+the+email+subject&utm_medium=email'
        self.assertEqual(append_tracking(url, params), a_url) 

        url = 'http://example.com?test=ssss&utm_source=Subject#frag'
        a_url = 'http://example.com?test=ssss&utm_source=Subject&utm_medium=email#frag'
        self.assertEqual(append_tracking(url, params), a_url) 
        

    def test_html_replacements(self):
       
        params = {'test': 'test'}

        html = """
               http://example.com <a href="http://example.com">http://example.com</a>.<br>
               <a href= "http://example.com">text</a>
               """
        r_html = """
               http://example.com <a href="http://example.com?test=test">http://example.com</a>.<br>
               <a href= "http://example.com?test=test">text</a>
               """

        self.assertEqual(replace_urls_html(html, params), 
                         str(BeautifulSoup(r_html, "html.parser")))



    def test_text_replacements(self):     

        params = {'test': 'test'}

        text = """
               http://example.com
               Url with period at end http://example.com.
               https url: https://example.com
               Longer url: http://www.example.com:43/somestuff/end.php
               """

        r_text = """
               http://example.com?test=test
               Url with period at end http://example.com?test=test.
               https url: https://example.com?test=test
               Longer url: http://www.example.com:43/somestuff/end.php?test=test
               """

        self.assertEqual(replace_urls_text(text, params), r_text)
