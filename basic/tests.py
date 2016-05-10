from django.core.urlresolvers import resolve
from django.test import TestCase
from basic.views import searchPage, findTweets


class searchPageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/searchPage/')
        self.assertEqual(found.func, searchPage)

class findTweetsTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/findTweets/')
        self.assertEqual(found.func, findTweets)

def test_home_page_returns_correct_html(self):
    request = HttpRequest()
    response = searchPage(request)
    self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
    self.assertIn(b'<title>Search Page</title>', response.content)
    self.assertTrue(response.content.endswith(b'</html>'))


def test_home_page_returns_correct_html(self):
    request = HttpRequest()
    response = searchPage(request)
    self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
    self.assertIn(b'<title>Results Page</title>', response.content)
    self.assertTrue(response.content.endswith(b'</html>'))
