from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='CIMS',
    version='0.1.0a',
    author='Marquel Rogers', 
    author_email='rogersmar2015@gmail.com',
    packages=find_packages(),
    long_description=open('README.md').read()
)