import os
from setuptools import setup, find_packages

VERSION = os.environ['RELEASE_VERSION']

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='Spot-Clity',
    version=VERSION,
    author='Cruz Milk',
    author_email='b.com',
    description=(
        'Control Spotify playback on any device through the command line.'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lostboysbangarang/Spot-Clity',
    license='MIT',

    packages=find_packages(),
    install_requires=[
        'Click',
        'PyInquirer',
        'tabulate',
    ],
    entry_points='''
        [console_scripts]
        wetPuss=cli.spotify:cli
    ''',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
)
