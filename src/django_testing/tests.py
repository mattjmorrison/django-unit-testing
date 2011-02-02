import unittest
import mock
from types import FunctionType
from django_testing import models

PREFIX = unittest.TestLoader.testMethodPrefix
QUERYSET_MOCK = mock.patch('django.db.models.Manager.get_query_set')

class QuerySetMockMetaClass(type):

    def __new__(meta, classname, bases, classDict):
        newClassDict = {}
        for attributeName, attribute in classDict.items():
            if type(attribute) == FunctionType and PREFIX == attributeName[:len(PREFIX)]:
                attribute = QUERYSET_MOCK(attribute)
            newClassDict[attributeName] = attribute
        return type.__new__(meta, classname, bases, newClassDict)

class MockedModelTestCase(unittest.TestCase):

    __metaclass__ = QuerySetMockMetaClass

    missing_return_value = "return value '%s' was not returned at the end of the chain"
    missing_from_chain = "%s not found in the call chain"

    def assertChained(self, mock_object, call_chain, value=None):
        calls = self._get_method_calls(mock_object)
        for mock_call in calls:
            for method_call_number, method_call in enumerate(call_chain):
                if method_call == mock_call:
                    if type(mock_call) != tuple:
                        return True
                    else:
                        new_call_chain = self._get_call_chain(call_chain, method_call_number)
                        return_value = self._get_return_value(method_call, mock_object)
                        if not new_call_chain:
                            return self._handle_end_of_chain(return_value, value)
                        if self.assertChained(return_value, new_call_chain, value):
                            return True

        raise AssertionError(self.missing_from_chain % call_chain)

    def _get_method_calls(self, mock_object):
        calls_and_properties = []
        calls = mock_object.method_calls
        for call in calls:
            if '.' not in call[0]:
                calls_and_properties.append(call)
        return calls_and_properties + mock_object._children.keys()

    def _get_return_value(self, method_call, mock_object):
        if '.' in method_call[0]:
            return_value = mock_object
            for node in method_call[0].split('.'):
                return_value = getattr(return_value, node)
            return_value = return_value.return_value
        else:
            return_value = getattr(mock_object, method_call[0]).return_value

        return return_value

    def _get_call_chain(self, call_chain, method_call_number):
        return call_chain[0:method_call_number] + call_chain[method_call_number + 1:]

    def _handle_end_of_chain(self, return_value, value):
        if not value or value == return_value:
            return True
        else:
            raise AssertionError(self.missing_return_value % value)

class Other(MockedModelTestCase):

    def setUp(self):
        self.manager = mock.Mock(spec=models.SampleManager)
        self.results = models.SampleManager.some_chained_call(self.manager)

        self.base_query = self.manager.base_query
        self.first_filter = self.base_query.ordering.filter
        self.second_filter = self.first_filter.return_value.filter
        self.third_filter = self.second_filter.return_value.filter
        self.return_value = self.third_filter.return_value

    def test_chained_calls_and_properties_with_no_return_value(self, queryset):
        self.assertChained(self.manager, [
            'base_query',
            ('filter', (), {'one':1}),
            ('filter', (), {'two':2}),
            ('filter', (), {'three':3}),
        ])

    def test_chained_calls_and_properties_with_return_value(self, queryset):
        self.assertChained(self.manager, [
            'base_query',
            ('filter', (), {'one':1}),
            ('filter', (), {'two':2}),
            ('filter', (), {'three':3}),
        ], self.results)

class Another(MockedModelTestCase):

    def test_manager_another_property_filter(self, queryset):
        result = models.SampleManager().filter_property
        self.assertChained(queryset.return_value, [
            ('filter', (), {'one':1, 'two':2}),
            ('filter', (), {'three':3}),
        ], result)
