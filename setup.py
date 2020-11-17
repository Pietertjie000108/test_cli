from setuptools import setup, find_packages

setup(
    name='example',
    version='0.1.0',
    packages=find_packages(include=['cli_print', 'cli_print.*']),
    entrypoints={
        'console_scripts': ['pitty=cli_print.cli_printer']
    }
)