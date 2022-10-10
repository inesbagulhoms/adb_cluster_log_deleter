import os
from setuptools import find_packages, setup
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="adb_cluster_log_deleter",
    version="1.0.0",
    author="Inês Bagulho",
    author_email="inesbagulho@microsoft.com",
    description="Azure Databricks Custom cluster log deleter",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    url="https://github.com/inesbagulhoms/adb_cluster_log_deleter.git",
    python_requires='>=3.6',
    packages=find_packages(include=['adb_cluster_log_deleter', 'adb_cluster_log_deleter.*'])
)
