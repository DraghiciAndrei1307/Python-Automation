
"""
    This is the setup.py script of the os_runner module.
"""

from setuptools import setup, find_packages

VERSION = '0.3.6'
DESCRIPTION = 'Performs os commands'
LONG_DESCRIPTION = 'A python package for os commands'


setup(
    name='ptyhon_os_runner',
    version=VERSION,
    author='Andrei Draghici',
    author_email='draghici.andrei12@yahoo.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[]
)
