from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'dataverse', 'version.py')) as f:
    exec(f.read(), version)

execute = {}
with open(os.path.join(_here, 'dataverse', 'app.py')) as f:
    exec(f.read())

setup(
    name='dataverse',
    version=version['__version__'],
    description=('App to get data fro dados.ifpb.edu.br, filtering and save on database.'),
    long_description=long_description,
    author='Rogério Araújo',
    author_email='rogerio.araujo@mail.com',
    url='https://github.com/rodgeraraujo/open-dataverse',
    license='MIT',
    packages=['dataverse'],
    run=execute['__main__'],
#   no dependencies in this example
#   install_requires=[
#       'dependency==1.2.3',
#   ],
#   no scripts in this example
#   scripts=['bin/a-script'],
    include_package_data=True,
    classifiers=[
        'Development Status :: Development',
        'Open Data :: Science/Research',
        'Programming Language :: Python :: 3.6'],
    )