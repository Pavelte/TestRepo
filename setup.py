from setuptools import setup,find_packages

dist = setup(
    name='supervisor2',
    packages=['test.tired'],
    entry_points={
        'console_scripts': ['fuck=test.tired.stam:main']},
    
)
