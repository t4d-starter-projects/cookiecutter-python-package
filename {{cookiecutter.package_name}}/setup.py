"""Setup Package Module"""

from pathlib import Path
from setuptools import find_packages, setup

HERE = Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="{{cookiecutter.package_name}}",
    version="0.1.0",
    description="{{cookiecutter.package_desc}}",
    long_description=README,
    long_description_content_type="text/markdown",
    url="{{cookiecutter.author_url}}",
    license="MIT",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    packages=find_packages(where=".", exclude=('tests',))
)
