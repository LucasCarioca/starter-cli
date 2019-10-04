from setuptools import setup

setup(
    name = 'starter-cli',
    version = '0.1.0',
    packages = ['cli', 'cli.module'],
    entry_points = {
        'console_scripts': [
            'starter-cli = cli.__main__:main' 
        ]
    }
)