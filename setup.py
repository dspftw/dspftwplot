# vim: expandtab tabstop=4 shiftwidth=4

from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), 'r') as f:
    long_description = f.read().strip()

with open(path.join(this_directory, 'VERSION'), 'r') as f:
    VERSION = f.read().strip()

setup(
    name='dspftwplot',
    version=VERSION,
    author='Bill Allen',
    author_email='billallen256@gmail.com',
    description='Plotting functions for the dspftw package.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='dsp signal processing plotting complex'.split(),
    url='https://github.com/dspftw/dspftwplot',
    packages=['dspftwplot'],
    install_requires=['dspftw', 'ipywidgets', 'matplotlib'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License'
    ]
)
