from setuptools import setup, find_packages

dist = setup(
    name='supervisor2',
    entry_points={
        'console_scripts': [
            'test3 = test.test2:main',
        ],
    },
)
