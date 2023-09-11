"""Python setup.py for cytomine_python_example package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("cytomine_python_example", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="cytomine_python_example",
    version=read("cytomine_python_example", "VERSION"),
    description="Awesome cytomine_python_example created by jeffersonfs",
    url="https://github.com/jeffersonfs/cytomine-python-example/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="jeffersonfs",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["cytomine_python_example = cytomine_python_example.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
