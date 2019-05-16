import os

import setuptools

with open('../README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

rootdir = os.path.join(os.path.dirname(__file__), '..', 'python-sdk')

setuptools.setup(
    name='nuscenes-devkit',
    version='1.0.2',
    author='Holger Caesar, Oscar Beijbom, Qiang Xu, Varun Bankiti, Alex H. Lang, Sourabh Vora, Venice Erin Liong, '
           'Chris Li, Sergi Widjaja et al.',
    author_email='nuscenes@nutonomy.com',
    description='The official devkit of the nuScenes dataset (www.nuscenes.org).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nutonomy/nuscenes-devkit',
    python_requires='>=3.6',
    install_requires=requirements,
    packages=setuptools.find_packages(rootdir),
    package_dir={'': rootdir},
    package_data={'': '*.json'},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
)
