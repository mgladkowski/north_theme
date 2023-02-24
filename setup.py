from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in north_theme/__init__.py
from north_theme import __version__ as version

setup(
	name="north_theme",
	version=version,
	description="Northportage Desk Theme for Frappe",
	author="Mike Gladkowski",
	author_email="mike@northportage.ca",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
