#!/usr/bin/env python

from setuptools import setup

setup(name="strava-tokengen",
      version="0.0.1",
      description="A simple OAuth token generator for the Strava API",
      url="https://github.com/pR0Ps/strava-tokengen",
      license="MPLv2",
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
      ],
      packages=["strava_tokengen"],
      package_data={"strava_tokengen": ["strava-tokengen.conf", "templates/*", "static/*"]},
      install_requires=["setuptools", "CherryPy>=11.1.0,<12.0.0.", "Jinja2>=2.9.6,<3.0.0", "stravalib>=0.6.6,<1.0.0"],
      entry_points={'console_scripts': ["strava-tokengen=strava_tokengen:run_server"]}
)
