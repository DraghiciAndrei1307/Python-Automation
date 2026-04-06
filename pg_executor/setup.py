"""
This package acts as a layer of
abstraction (a CLI interface)
between the user and the pg_runner.
"""

from setuptools import setup, find_packages


VERSION = '0.1.2'
DESCRIPTION = 'This is the pg_executor module.'
LONG_DESCRIPTION = (
    'This is the CLI interface that stands '
    'between module the user and the pg_runner.'
)
AUTHOR = 'Andrei Draghici'
AUTHOR_EMAIL = 'draghici.andrei12@yahoo.com'

setup(
    name='pg_executor_draghici_andrei',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Andrei Draghici',
    author_email='draghici.andrei12@yahoo.com',
    url='https://github.com/draghiciandrei1307/python-automation',
    packages=find_packages(),
    install_requires=[
        'click',
        'pg_runner_draghici_andrei'
    ],
    entry_points={
        'console_scripts': [
            # 'terminal command = package.file:function'
            'pg_executor=pg_executor.pg_executor:cli',
        ],
    },

)





