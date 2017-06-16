import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'Babel==2.4.0',
    'beautifulsoup4==4.6.0',
    'Chameleon==3.1',
    'coverage==4.4.1',
    'hupper==1.0',
    'Jinja2==2.9.6',
    'lingua==4.13',
    'Mako==1.0.6',
    'MarkupSafe==1.0',
    'PasteDeploy==1.5.2',
    'polib==1.0.8',
    'py==1.4.34',
    'Pygments==2.2.0',
    'pyramid==1.8.4',
    'pyramid-debugtoolbar==4.1',
    'pyramid-jinja2==2.7',
    'pyramid-mako==1.0.2',
    'pytest==3.1.2',
    'pytest-cov==2.5.1',
    'pytz==2017.2',
    'repoze.lru==0.6',
    'six==1.10.0',
    'translationstring==1.3',
    'venusian==1.1.0',
    'waitress==1.0.2',
    'WebOb==1.7.2',
    'WebTest==2.0.27',
    'zope.deprecation==4.2.0',
    'zope.interface==4.4.1',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup(
    name='scrapper',
    version='0.0',
    description='scrapper',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Musavengana Zirebwa',
    author_email='musaz01@gmail.com',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = scrapper:main',
        ],
    },
)
