import unittest
import mock

from django_testing import models

class Tests(unittest.TestCase):

    @mock.patch('django_testing.models.Sample.objects')
    def test_something(self, objects):
        samples = models.Sample.objects.all()
        self.assertEqual(objects.all.return_value, samples)

class Other(unittest.TestCase):

    def test_another_thing(self):
        self.fail("hi!!!")
        