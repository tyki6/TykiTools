import re

import setuptools

with open("README.md") as f:
    long_description = f.read()
f.close()

setuptools.setup(
    name="tykitools",
    version="0.0.1",
    author="tyki6",
    author_email="matthieubouamama@gmail.com",
    description="MultiTools OSINT Created by a tiktoker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tyki6/TykiTools",
    entry_points={"console_scripts": ["tykitools = main:cli"]},
    packages=setuptools.find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.10",
)
