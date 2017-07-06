from setuptools import setup, find_packages


dist = setup(
    name='test',
    description="A system for controlling process state under UNIX",
    author="Chris McDonough",
    author_email="chrism@plope.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'test2 = test:main'
        ],
    },
)
