#!/usr/bin/env python
from setuptools import setup

import versioneer

requires = open("requirements.txt").read().strip().split("\n")

setup(
    name="intake-asammdf",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="SQL plugin for Intake",
    url="https://github.com/AutomotiveDevOps/intake-asammdf",
    maintainer="Martin Durant",
    maintainer_email="mdurant@anaconda.com",
    license="BSD",
    py_modules=["intake_asammdf"],
    packages=["intake_asammdf"],
    package_data={"": ["*.csv", "*.yml", "*.html"]},
    entry_points={
        "intake.drivers": [
            "sql = intake_asammdf.intake_asammdf:SQLSource",
            "sql_cat = intake_asammdf.sql_cat:SQLCatalog",
            "sql_auto = intake_asammdf.intake_asammdf:SQLSourceAutoPartition",
            "sql_manual = intake_asammdf.intake_asammdf:SQLSourceManualPartition",
        ]
    },
    include_package_data=True,
    install_requires=requires,
    long_description=open("README.rst").read(),
    zip_safe=False,
)
