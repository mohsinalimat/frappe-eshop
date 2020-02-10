# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in eshop/__init__.py
from eshop import __version__ as version

setup(
	name='eshop',
	version=version,
	description='App for shop',
	author='anupamvs',
	author_email='anupam@erpnext.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
