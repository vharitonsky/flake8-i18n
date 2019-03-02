# -*- coding: utf-8 -*-
from setuptools import setup


short_description = 'Warns about incorrect gettext usage.'


long_description = '{0}\n{1}'.format(
    open('README.rst').read(),
    open('CHANGES.rst').read(),
)


setup(
    name='flake8-i18n',
    version='0.1.0',
    description=short_description,
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Free',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Quality Assurance',
    ],
    keywords='pep8 flake8 i18n',
    author='Vitaliy Kharitonskiy',
    author_email='gil.gnome@gmail.com',
    url='https://github.com/vharitonsky/flake8-i18n',
    license='Free',
    py_modules=['flake8_i18n'],
    include_package_data=True,
    test_suite='run_tests',
    zip_safe=False,
    install_requires=[
        'flake8 >= 3.0.0',
    ],
    entry_points={
        'flake8.extension': [
            'I00 = flake8_i18n:Flake8i18n',
        ],
    },
)
