#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-eventbrite",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_eventbrite"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-eventbrite=tap_eventbrite:main
    """,
    packages=["tap_eventbrite"],
    package_data = {
        "schemas": ["tap_eventbrite/schemas/*.json"]
    },
    include_package_data=True,
)
