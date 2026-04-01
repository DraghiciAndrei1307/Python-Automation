
"""
    This is the setup.py script of the os_runner module.
"""

from setuptools import setup, find_packages

VERSION = '0.3.12'
DESCRIPTION = 'Performs os commands'
LONG_DESCRIPTION = 'A python package for os commands'


setup(
    name='os_runner_draghici_andrei',
    version=VERSION,
    author='Andrei Draghici',
    author_email='draghici.andrei12@yahoo.com',
    url='https://pypi.pkg.github.com/draghiciandrei1307/python-automation/',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[]
)
