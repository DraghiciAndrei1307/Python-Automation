from setuptools import setup, find_packages

VERSION = '0.3.1'
DESCRIPTION = 'Performs os commands'
LONG_DESCRIPTION = 'A python package for os commands'


setup(
    name='os_runner',
    version=VERSION,
    author='Andrei Draghici',
    author_email='draghici.andrei12@yahoo.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[ # here you will put your dependencies

    ]
)

