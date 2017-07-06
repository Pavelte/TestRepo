from setuptools import setup

dist = setup(
    name='supervisor2',
    entry_points={
        'console_scripts': [
            'test5=test:stam',
        ],
    },
)
