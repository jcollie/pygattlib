#!/usr/bin/python
# -*- mode: python; coding: utf-8 -*-

import subprocess
from distutils.core import setup, Extension


glib_headers = subprocess.check_output("pkg-config --cflags glib-2.0".split())
glib_headers = glib_headers.strip().split("-I")
glib_headers = [x.strip() for x in glib_headers if x]

setup(
    name = 'gattlib',
    version = '0.20141222',
    description = "Library to access Bluetooth LE devices",
    author = "Oscar Acena",
    author_email = "oscar.acena@gmail.com",
    url = "https://bitbucket.org/OscarAcena/pygattlib",

    ext_modules = [
        Extension(
            'gattlib',
            ['src/gattservices.cpp',
             'src/bindings.cpp',
             'src/gattlib.cpp',
             'src/bluez/lib/uuid.c',
             'src/bluez/attrib/gatt.c',
             'src/bluez/attrib/gattrib.c',
             'src/bluez/attrib/utils.c',
             'src/bluez/attrib/att.c',
             'src/bluez/src/shared/crypto.c',
             'src/bluez/src/log.c',
             'src/bluez/btio/btio.c'],
            libraries = ["boost_python", "boost_thread", "bluetooth"],
            include_dirs = glib_headers + [
                'src/bluez',
            ],
            define_macros = [('VERSION', '"5.25"')],
        )
    ],
)
