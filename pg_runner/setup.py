"""
    This is the setup.py script of the pg_runner module.
"""

from setuptools import setup, find_packages

VERSION = '0.2.5'
DESCRIPTION = (
    'This is the pg_runner. It is used to perform '
    'PostgreSQL management operations.'
)
LONG_DESCRIPTION = (
    'You can think of this module as the 2nd '
    'layer of this whole Python infrastructure. '
    'It uses the os_runner package in order to '
    'be able to perform simple PostgreSQL management '
    'operations.'
)


setup(
    name='pg_runner_draghici_andrei',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Andrei Draghici',
    author_email='draghici.andrei12@yahoo.com',
    url='https://github.com/draghiciandrei1307/python-automation',
    packages=find_packages(),
    install_requires=[
        'os_runner_draghici_andrei'
    ]
)
