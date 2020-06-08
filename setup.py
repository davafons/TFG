# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ""
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.rst")
if os.path.exists(readme_path):
    with open(readme_path, "rb") as stream:
        readme = stream.read().decode("utf8")


setup(
    long_description=readme,
    name="dial-core",
    version="0.21a0",
    description="Deep Learning, node-based framework",
    python_requires="<=3.8.3,>=3.6.0",
    project_urls={
        "homepage": "https://github.com/dial-app/dial-core",
        "repository": "https://github.com/dial-app/dial-core",
    },
    author="David Afonso",
    author_email="davafons@gmail.com",
    license="GPL-3.0-only",
    keywords="deep-learning",
    packages=[
        "dial_core",
        "dial_core.datasets",
        "dial_core.datasets.datatype",
        "dial_core.datasets.io",
        "dial_core.node_editor",
        "dial_core.notebook",
        "dial_core.plugin",
        "dial_core.project",
        "dial_core.utils",
        "dial_core.utils.log",
    ],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        "dependency-injector==3.*,>=3.15.6",
        "nbformat==5.*,>=5.0.5",
        "pillow==7.*,>=7.1.2",
        "rope==0.*,>=0.16.0",
        "tensorflow==2.*,>=2.2.0",
        "toml==0.*,>=0.10.0",
    ],
    extras_require={
        "dev": [
            "black==19.*,>=19.10.0.b0",
            "docstr-coverage==1.*,>=1.0.5",
            "flake8==3.*,>=3.7.9",
            "isort==4.*,>=4.3.21",
            "mypy==0.*,>=0.761.0",
            "pre-commit==2.*,>=2.1.1",
            "pylint==2.*,>=2.4.4",
            "pytest==5.*,>=5.2.0",
            "pytest-cov==2.*,>=2.4.0",
            "sphinx==2.*,>=2.4.4",
            "sphinx-autodoc-typehints==1.*,>=1.10.3",
            "sphinx-rtd-theme==0.*,>=0.4.3",
            "taskipy==1.*,>=1.1.3",
            "tox==3.*,>=3.14.5",
        ]
    },
)
