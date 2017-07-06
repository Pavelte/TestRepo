from setuptools import setup,find_packages

dist = setup(
    name='supervisor2',
    packages=['test', 'test.tired','test.tired.stam'],
    entry_points={
        'console_scripts': ['fuck=test.tired.stam:main']},
    
)
