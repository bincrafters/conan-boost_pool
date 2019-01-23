#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostPoolConan(base.BoostBaseConan):
    name = "boost_pool"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_pool"
    lib_short_names = ["pool"]
    header_only_libs = ["pool"]
    cycle_group = "boost_level11group"
    b2_requires = [
        "boost_level11group",
    ]


