from setuptools import setup, find_packages

dist = setup(
    name='supervisor2',
    entry_points={
        'console_scripts': [
            'test5=test:main',
        ],
    },
)
