#!/usr/bin/env python3

from setuptools import setup, Extension

luastack = Extension('pygmod._luastack', sources=['python_extensions/_luastack.cpp'], include_dirs=['python_extensions'])

setup(
    name='PyGmod',
    packages=['gmod', 'pygmod'],
    ext_modules=[luastack],
    setup_requires=['pytest-runner'],
    tests_require=[
        'coverage',
        'pytest',
        'pytest-cov',
        'pytest-pylint'
    ],
    zip_safe=False
)
