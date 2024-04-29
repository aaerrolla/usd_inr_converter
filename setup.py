from setuptools import setup, find_packages

setup(
    name="usd_inr_converter",
    version='0.1',
    packages=find_packages(),
    install_requires=['requests'],
    auhor='Anjaneyulu Aerrolla',
    author_email="aaerrolla@gmail.com",
    description='A Simple currency converter package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aaerrolla/usd_inr_converter',
)