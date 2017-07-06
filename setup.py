from setuptools import setup,find_packages

dist = setup(
    name='supervisor2',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['fuck=stam']},
    
)
