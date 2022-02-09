# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:03:09 2022

@author: C039741
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='kraftTool',
    version='1.0.0',
    author='Himanshu Bajpai',
    description='Testing installation of kraftTool',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/BajpaiHimanshuABI/kraftTool',
    project_urls = {
        "Bug Tracker": "https://github.com/BajpaiHimanshuABI/kraftTool/issues"
    },
    license='MIT',
    packages=['kraftTool'],
    install_requires=['requests'],
)