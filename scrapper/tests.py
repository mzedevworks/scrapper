import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import home
        request = testing.DummyRequest()
        info = home(request)
        self.assertEqual(info, {})


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from scrapper import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Want to be ready for your future? All you need is practice.' in res.body)
        self.assertTrue(b'Enter a valid wiki url in the form below and we will scrap it for you' in res.body)
        self.assertTrue(b'Go' in res.body)
        self.assertTrue(b'How ironic that a site called Siyavula is only being offered in English.' in res.body)
        self.assertTrue(b'With this decolonisation of education mantra and all it will be a great move to translate '
                        b'the site into some' in res.body)
        self.assertTrue(b'local languages Zulu, Xhosa and Afrikaans to lure everyone. This will be my first project'
                        in res.body)

    def test_root_post(self):
        #Test if the wiki url is invalid
        res = self.testapp.post('/', {'url': 'https://en.wikipedia.scscascsorg/wiki/The_Last_of_Us'}, status=200)
        self.assertIn(b'Invalid wikipedia url format entered. Try again. Dont leave out the https:// or http://',
                      res.body)
        #Test for an invalid wiki url
        res = self.testapp.post('/', {'url': 'https://www.google.com'}, status=200)
        self.assertIn(b'The url you entered is not a valid wikipedia url', res.body)

        # Test for a valid wiki url
        res = self.testapp.post('/', {'url': 'https://en.wikipedia.org/wiki/The_Last_of_Us'}, status=200)
        self.assertIn(b'You have successfully managed to scrape something and below is the table of contents', res.body)
        self.assertIn(b'Contents', res.body)

