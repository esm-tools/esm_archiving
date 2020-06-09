#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().splitlines()

setup_requirements = []

test_requirements = ["pyfakefs"]

setup(
    author="Paul Gierz",
    author_email="pgierz@awi.de",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="ESM Archiving gives you modern tools for putting your run on the tape",
    entry_points={"console_scripts": ["esm_archive=esm_archiving.cli:main"]},
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="esm_archiving",
    name="esm_archiving",
    packages=find_packages(
        include=["esm_archiving", "esm_archiving.database", "esm_archiving.external"]
    ),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/pgierz/esm_archiving",
    version="4.0.0",
    zip_safe=False,
)
