from setuptools import setup

long_description = open('README.rst').read()

setup(
    name="datazilla-metrics",
    version="0.1",
    description="Test metrics for Datazilla",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        ],
    keywords="datazilla metrics",
    author="Carl Meyer",
    author_email="cmeyer@mozilla.com",
    url="https://github.com/mozilla/datazilla-metrics",
    license="BSD",
    packages=["dzmetrics"],
    install_requires=["scipy"],
    zip_safe=False,
    test_suite="dzmetrics.tests",
    )
