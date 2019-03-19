from setuptools import setup, find_packages

setup(
    name='mypackagee',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://https://github.com/THUBELIHLEd/mypackagee.git',
    author='lucky ndimande',
    author_email='thube7langa@gmail.com'
)
