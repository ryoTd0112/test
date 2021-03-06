#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import isatex

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

setup_requirements = []

test_requirements = []

description = "iSATex is an ideal software package for all uses of Raman microscope and/or FT-IR. Open-source-software development from the researcher’s perspectives would be complementary with the development of the modern analytical geosciences."

setup(
    author="Ryo Tandai",
    author_email='ryo.s1042@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="iSATex is an ideal software package for all uses of Raman microscope and/or FT-IR. Open-source-software development from the researcher’s perspectives would be complementary with the development of the modern analytical geosciences.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='isatex',
    name='isatex',
    packages=find_packages(include=['isatex', 'isatex.*']),
    setup_requires=setup_requirements,
    url='https://github.com/ryoTd0112/isatex',
    # version=isatex.__version__,
    version='1.0.2',
    zip_safe=False,
    entry_points="""
    [console_scripts]
    iSATex = isatex.main:ConsoleLaunch
    """
)
