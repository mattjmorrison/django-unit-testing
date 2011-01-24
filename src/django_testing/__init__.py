from django.test.simple import DjangoTestSuiteRunner

class TestSuiteRunner(DjangoTestSuiteRunner):

    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        suite = self.build_suite(test_labels, extra_tests)
        result = self.run_suite(suite)
        return self.suite_result(suite, result)