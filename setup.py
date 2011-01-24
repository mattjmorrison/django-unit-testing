from setuptools import setup

setup(
    name="django-unit-test",
    version="dev",
    description="Unit testing helpers for Django",
    author="Matthew J. Morrison",
    author_email="mattj.morrison@gmail.com",
    include_package_data=True,
    package_dir={'':'src'},
    packages=('django-testing', ),
    install_requires = (
        'south',
        'django-debug-toolbar',
        'mock',
        'unittest-xml-reporting',
        'coverage',
        'pylint',
    ),
)
