import setuptools
import re

long_description = ''
with open('README.md', 'r') as fh:
    long_description = fh.read()

version = ''
with open('penguinpi/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

requirements = ['requests', 'opencv_python', 'numpy']

try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    pass

setuptools.setup(
    name='penguinpi',
    url='https://github.com/cirrus-robotics/penguinpi',
    project_urls={
        'Documentation': 'https://github.com/cirrus-robotics/penguinpi/README.md',
        'Issue tracker': 'https://github.com/cirrus-robotics/penguinpi/issues',
    },
    version=version,
    author='Cirrus Robotics Pty Ltd',
    description='Library for communicating with and controlling the PenguinPi robot platform.',
    long_description=long_description,
    license='MIT',
    long_description_content_type='text/markdown',
    install_requires=requirements,
    packages=['penguinpi'],
    python_requires='>=2.7',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)