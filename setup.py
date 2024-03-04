from setuptools import setup, find_packages

setup (
    name='excel2flapjack',
    version='1.0.2',
    packages=find_packages(where='src'),
    package_dir={'':'src'},
)