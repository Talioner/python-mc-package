from setuptools import setup, find_packages

setup(
    name='python-mc-package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A test python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Talioner/python-mc-package',
    author='Kacper Tokarczyk',
    author_email='226021@student.pwr.edu.pl'
)
