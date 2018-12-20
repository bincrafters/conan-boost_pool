#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostPoolConan(base.BoostBaseConan):
    name = "boost_pool"
    url = "https://github.com/bincrafters/conan-boost_pool"
    lib_short_names = ["pool"]
    header_only_libs = ["pool"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_integer",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_winapi"
    ]
