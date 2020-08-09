import setuptools

__project__ = "HashChecker-pkg-SurajApps"
__version__ = "0.0.1"
__description__ = "A python module to see if a file has been tampered with, by comparing checksums."
__packages__ = ["HashChecker"]
__author__ = "Suraj Apps"
__url__ = "https://github.com/SurajApps/HashChecker"
__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: System Administrators",
    "Programming Language :: Python :: 3",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Topic :: System :: Hardware",
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=__project__,
    version=__version__,
    author=__author__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    packages=__packages__,
    classifiers=__classifiers__,
    python_requires='>=3.6',
    entry_points=
    {"console_scripts": ["hash-checker = HashChecker.HashChecker:Check"]}
)
